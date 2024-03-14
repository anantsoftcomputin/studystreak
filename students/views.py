from django.shortcuts import render
from .serializers import StudentSerializers, StudentRetUpdDelSerializers, StudentRetUpdDelUserSerializers
from .models import Student
from rest_framework import generics
from django.contrib.auth.models import AnonymousUser, User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class StudentView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get_queryset(self):
        user = self.request.user
        # user = request.user
        if isinstance(user, AnonymousUser):
            return Student.objects.none() 

        return Student.objects.filter(user=user)
class StudentRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentRetUpdDelSerializers

    
class StudentRetUpdDelUserView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentRetUpdDelUserSerializers

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
    

class Student_List_View_Dashboard(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


from django.http import JsonResponse
from package.models import Package

def PackageIdwiseStudentGetView(request, package_id):
    try:
        package = Package.objects.get(pk=package_id)
        students = package.student_set.all() 
        serialized_students = []  
        if students.exists():
            for student in students:
                serialized_student = {
                    'id': student.id,
                    'user_name': student.user.username,  
                    'user_first_name': student.user.first_name
                }
                serialized_students.append(serialized_student)
            return JsonResponse({'students': serialized_students}, status=200)
        else:
            return JsonResponse({'message': 'No students available in package'}, status=200)
    except Package.DoesNotExist:
        return JsonResponse({'error': 'Package not found'}, status=404)