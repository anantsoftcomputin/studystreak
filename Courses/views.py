from django.contrib.auth.models import Group, User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# from coursedetail.models import Quiz_Question, QuizOption
# from coursedetail.serializers import QuizOptionListSerializers, Quiz_QuestionListSerializers
from master.models import (AdditionalResource, CourseMaterial,
                           LessonAssignment, LessonAttachment, batch)
from master.serializers import (AdditionalResourceListSerializers,
                                CourseMaterialListSerializers,
                                LessonAssignmentSerializer,
                                LessonAttachmentSerializer)

from .models import Course, YoutubeDataRecord
from .serializers import (Course_List_Serializers_forpackage,
                          CourseCreateSerializers, CourseListSerializers,
                          CourseRetUpdDelSerializers, GroupSerializer,
                          UserSerializer, UserSerializerforinstructor,
                          YoutubeDataSerializer)
from rest_framework_simplejwt.authentication import JWTAuthentication


class CourseListView(generics.ListCreateAPIView):
    permission_classes = []
    queryset = Course.objects.all()
    serializer_class = CourseListSerializers

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['Category__name', 'Level__name', ]
    search_fields = ['Course_Title', ]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CourseCreateSerializers
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        data = response.data

        for course_data in data:
            course_id = course_data['id']
            course_materials = CourseMaterial.objects.filter(course_id=course_id)
            additional_resources = AdditionalResource.objects.filter(course_id=course_id)

            course_materials_serializer = CourseMaterialListSerializers(course_materials, many=True, read_only=True)
            additional_resources_serializer = AdditionalResourceListSerializers(additional_resources, many=True, read_only=True)

            course_data['course_materials'] = course_materials_serializer.data
            course_data['additional_resources'] = additional_resources_serializer.data

        return Response(data)

class CourseRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseRetUpdDelSerializers
    
    def get_serializer_context(self):
        try:
            return {'user':self.request.user.student}
        except Exception as e :
            return {'user':None}
        
################# List of all course to use in package model ##################

class Course_list_forpackage(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = Course_List_Serializers_forpackage
    

################# Get List of all users ##################

class CourseTutorListView(generics.ListAPIView):
    queryset = User.objects.filter(groups__name='Tutor')
    serializer_class = UserSerializer



class CourseInstructorListView(generics.ListAPIView):
    # queryset = Group.objects.all()
    queryset = User.objects.filter(groups__name='Instructor')
    serializer_class = UserSerializerforinstructor
    
from rest_framework.views import APIView


class YoutubeDataApiView(APIView):
    queryset = YoutubeDataRecord.objects.all()
    
    def post(self, request):
        serializer = YoutubeDataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            print(data)
            timestamp = data.pop('timestamp')
            data['student'] = request.user.student
            instance, created = self.queryset.update_or_create(**data, defaults={'timestamp':timestamp})
            data['timestamp'] = timestamp
            if created:
                return Response(serializer.data, 201)
            else:
                return Response(serializer.data, 200)