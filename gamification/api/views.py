from django.db.models import F
from django.db.models.aggregates import Sum
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from django.contrib.contenttypes.models import ContentType

from django.http import StreamingHttpResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .common import model_mapper
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from ..models import Badge, FlashCard, Gamification, PointHistory
from .serializers import (
    BadgeSerializer,
    FlashCardSerializer,
    GamificationCreateSerializer,
)
from ..utils import save_points_and_publish_message


class FlashCardViewSet(ModelViewSet):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer


class GamificationViewSet(ViewSet):
    queryset = Gamification.objects.all()

    def create(self, request):
        serializer = GamificationCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "Bad request"}, status=status.HTTP_201_CREATED)

    def list(self, request):
        qs = Gamification.objects.all()
        data = GamificationCreateSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='models')
    def models(self, request):
        return Response(model_mapper.get_model_dict(), 200)

    @action(detail=False, methods=['get'], url_path='objects')
    def objects(self, request):
        model = request.query_params.get('model')
        if not model:
            return Response({}, 204)
        model_class = model_mapper.get_model_for_rep(model)
        if model_class:
            return Response([{'object_id': i.id, 'rep_name': i.__str__()} for i in model_class.objects.all()], 200)
        else:
            return Response({"error": 'Bad request'}, 400)


class PointHistoryViewSet(ViewSet):
    def get_queryset(self):
        user = self.request.user
        try:
            user.student
        except Exception as e:
            raise ValidationError(f"user {user.username} not registered as student")
        return PointHistory.objects.filter(student=user.student).select_related("student","gamification")

    def get(self, request):
        queryset = (
            self.get_queryset()
            .annotate(
                points=F("gamification__points"),
                model=F("gamification__content_type__model"),
                object_id=F("gamification__object_id"),
            )
            .values("created_at", "points", 'model',"object_id")
            .order_by("-created_at")
        )
        for i in queryset:
            print(i)
            i['model'] = model_mapper.get_model_for_rep(i['model'],return_rep=True)
        return Response(list(queryset), 200)

    def create(self, request):
        try:
            student = request.user.student
        except Exception as e:
            return Response('User is not registered as student', 400)

        model = request.data.get('model')
        object_id = request.data.get('object_id')

        if not model or not object_id:
            return Response({"error": 'model or object_id cannot be blank'}, 400)

        model_class = model_mapper.get_model_for_rep(model)

        if model_class:
            content_type = ContentType.objects.get_for_model(model_class)
            g_object = Gamification.objects.filter(content_type=content_type, object_id=object_id)
            if g_object.exists():
                obj, created = PointHistory.objects.get_or_create(student=student, gamification=g_object[0], )
                if created:
                    return Response({'msg': "Created"}, 201)
                else:
                    return Response({"msg": "already exists"}, 200)
            else:
                return Response('Gamification is not available for this object_id.',400)
        return Response('model is not available for the points.', 400)


class FlashCardPointView(APIView):
    class FlashCardSerializer(serializers.Serializer):
        flashcard = serializers.PrimaryKeyRelatedField(queryset=FlashCard.objects.all())

    def post(self, request):
        serializer = self.FlashCardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                student = getattr(self.request.user, "student")
            except Exception as e:
                return Response(
                    {"error": "This user is not registered as student"}, 400
                )

            flashcard = serializer.validated_data.get("flashcard")

            if not flashcard.g.all().exists():
                return Response({"msg": "flash card is not registered for points"}, 200)

            save_points_and_publish_message(
                flashcard.g.all().first(), self.request.user
            )
            return Response(None, 200)


class BadgeViewSet(ModelViewSet):
    serializer_class = BadgeSerializer
    queryset = Badge.objects.all()




def Notification(request):
    def event_stream(user):
        last_id = -1
        while True:
            notification = PointHistory.objects.order_by('-created_at')[0]
            if last_id < notification.id:
                last_id = notification.id
                yield f'data: {notification.gamification.points}\n\n'

    response = StreamingHttpResponse(event_stream(request.user), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    return response
