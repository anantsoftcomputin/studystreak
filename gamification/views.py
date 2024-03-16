from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from coursedetail.models import Lesson
from coursedetail.serializers import LessonListSerializers
from Courses.models import Course
from Courses.serializers import CourseListSerializers
from Create_Test.models import Exam, FullLengthTest, module
from Create_Test.serializers import FLTCreateSerializer
from Create_Test.serializers import ModuleListSerializers as PracticeSerializer
from exam.serializers import ExamSerializers
from LiveClass.models import Live_Class

from .models import FlashCard, Gamification
from .serializers import FlashCardSerializer, GamificationCreateSerializer


class FlashCardView(ListCreateAPIView):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer


class gamificationCreateView(APIView):
    def post(self, request):
        serializer = GamificationCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("bad request", status=status.HTTP_201_CREATED)


class gamificationListView(APIView):
    def get(self, request):
        qs = Gamification.objects.all()
        data = []

        for q in qs:

            if isinstance(q.content_object, FlashCard):
                temp_data = FlashCardSerializer(q.content_object).data
                temp_data.update({"model": "flashcard"})
                data.append(temp_data)

            elif isinstance(q.content_object, Lesson):
                temp_data = LessonListSerializers(q.content_object).data
                temp_data.update({"model": "lesson"})
                data.append(temp_data)

            elif isinstance(q.content_object, Course):
                temp_data = CourseListSerializers(q.content_object).data
                temp_data.update({"model": "course"})
                data.append(temp_data)

            elif isinstance(q.content_object, Exam):
                temp_data = ExamSerializers(q.content_object).data
                temp_data.update({"model": "exam"})
                data.append(temp_data)

            elif isinstance(q.content_object, FullLengthTest):
                temp_data = FLTCreateSerializer(q.content_object).data
                temp_data.update({"model": "fulllengthtest"})
                data.append(temp_data)

            elif isinstance(q.content_object, module):
                temp_data = PracticeSerializer(q.content_object).data
                temp_data.update({"model": "module"})
                data.append(temp_data)

            elif isinstance(q.content_object, Live_Class):
                pass

        # serializer = json.loads(serializers.serialize('json', Gamification.objects.all()))
        return Response(data, status=status.HTTP_200_OK)
