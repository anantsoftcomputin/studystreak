

import os
import time

from django.conf import settings
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from Create_Test.models import FullLengthTest, module
from exam.serializers import AnswerSerializer
from ExamResponse.models import Studentanswer

from .models import SpeakingBlockAnswer, SpeakingResponse
from .serializers import (
    FLTAnswerSerializer,
    PracticeTestAnswerSerializer,
    SpeakingAnswerBlockSerializer,
    SpeakingAnswerSerializer,
    StudentAnswerSerializers,
    StudentanswerSerializers,
    StudentanswerSpeakingResponseSerializers,
)

# class GetAnswerData:
#     fields_mappings = {'r':'Reading', 'l':'Listening', 's':'Speaking', 'w':'Writing'}

#     res_data = {'correct_answers':{},
#                 'student_answers':{}}
    
#     def __get_data(self,practice_set_instance,field:Literal['r','w','s','l']):
#         field = self.fields_mappings['field']
        
#         for i in practice_instance_data:

#             for j in getattr(practice_set_instance, i).all():
#                 serializer = AnswerSerializer(j.answers.all(), many=True)
#                 if res_data['correct_answers'].get(i,None):
#                     res_data['correct_answers'][i].append({'block_id':j.id, "answers":serializer.data})
#                 else:
#                     res_data['correct_answers'][i] = [{'block_id':j.id, "answers":serializer.data}]

#                 studentanswer_instance = Studentanswer.objects.filter(Practise_Exam=practice_set_instance,user=self.request.user, exam = j).first()
#                 if (studentanswer_instance):
#                     student_data = StudentAnswerSerializers(studentanswer_instance.student_exam.all(), many=True).data
#                     if res_data['student_answers'].get(i,None):
#                         res_data['student_answers'][i].append({'block_id':j.id, "answers":student_data})
#                     else:
#                         res_data['student_answers'][i] = [{'block_id':j.id, "answers":student_data}]


#         return res_data
        
#     def get_reading_data(self,practice_set_instance):
#         self.__get_data(practice_set_instance,field='r')
    
#     def get_writing_data(self,practice_set_instance):
#         self.__get_data(practice_set_instance,field='w')
    
#     def get_listening_data(self, practice_set_instance):
#         self.__get_data(practice_set_instance,'l')
    
#     def get_speaking_data(self,)
        
#     def get_speaking_data():...

class GetAnswerDataMixin:
    
    practice_instance_data = {'r':'Reading', 'l':'Listening','w':'Writing'}
    
    def get_answers(self, practice_set_instance):
        res_data = {'correct_answers':{},
            'student_answers':{}}
           
        for i in list(self.practice_instance_data.values()):
    
            for j in getattr(practice_set_instance, i).all():
                serializer = AnswerSerializer(j.answers.all(), many=True)
                if res_data['correct_answers'].get(i,None):
                    res_data['correct_answers'][i].append({'block_id':j.id, "answers":serializer.data})
                else:
                    res_data['correct_answers'][i] = [{'block_id':j.id, "answers":serializer.data}]

                studentanswer_instance = Studentanswer.objects.filter(Practise_Exam=practice_set_instance,user=self.request.user, exam = j).first()
                if (studentanswer_instance):
                    student_data = StudentAnswerSerializers(studentanswer_instance.student_exam.all(), many=True).data
                    if res_data['student_answers'].get(i,None):
                        res_data['student_answers'][i].append({'block_id':j.id, "answers":student_data})
                    else:
                        res_data['student_answers'][i] = [{'block_id':j.id, "answers":student_data}]


        return res_data
    
    def get_speaking_data(self, practice_set_instance):
        res_data = {'student_answers':{}}
        
        i = "Speaking"
        for j in getattr(practice_set_instance, i).all():
            
            studentanswer_instance = Studentanswer.objects.filter(
                                                    Practise_Exam=practice_set_instance,
                                                    user=self.request.user,
                                                    speaking_block = j).first()
            if (studentanswer_instance):
                print('thid')
                print((w:=studentanswer_instance))
                if res_data['student_answers'].get(i,None):
                    res_data['student_answers'][i].append({'block_id':j.id, "band":studentanswer_instance.band})
                else:
                    res_data['student_answers'][i] = [{'block_id':j.id, "band":studentanswer_instance.band}]

        return res_data
class PracticeAnswersView(GetAnswerDataMixin,APIView):
    
    def get(self, request, pk):
        try:
            module_instance = module.objects.get(pk=pk)
        except module.DoesNotExist:
            return Response(status=404)
        
        res_data = self.get_answers(module_instance)
        speaking_data = self.get_speaking_data(module_instance)
        res_data['student_answers'].update(speaking_data['student_answers'])
        
        res_data["name"] = module_instance.Name
        res_data["difficulty_level"] = module_instance.difficulty_level
        return Response(res_data)
    
class StudentAnswerListView(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    queryset = Studentanswer.objects.all()
    serializer_class = StudentanswerSerializers

class SpeakingAnswerListView(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    queryset = Studentanswer.objects.all()
    serializer_class = StudentanswerSpeakingResponseSerializers

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)
    


class PracticeTestAnswerCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PracticeTestAnswerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()  
            return Response({'msg':'created'}, 201)
    
class FLTAnswers(GetAnswerDataMixin,APIView):
    def get(self, request, flt_id):
        try:
            flt_instance = FullLengthTest.objects.get(pk=flt_id)
        except FullLengthTest.DoesNotExist:
            return Response('record with this id does not exists',400)

        reading_set_data = self.get_answers(flt_instance.reading_set)
        speaking_set_data = self.get_speaking_data(flt_instance.speaking_set)
        writing_set_data = self.get_answers(flt_instance.writing_set)
        listening_set_data = self.get_answers(flt_instance.listening_set)

        return Response({
            "reading_set":reading_set_data,
            "speaking_set":speaking_set_data,
            "writing_set":writing_set_data,
            "listening_set":listening_set_data,
        }, 200)
    

        
class FLTAnswerCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = FLTAnswerSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'created'}, 201)





class SaveSpeakingAnswerFileView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request, *args, **kwargs):
        user = str(request.user.username)
        
        file=request.FILES.get("file")
        exam_id = request.data.get("exam_id",None)
        extension = request.data.get("extension",None)
        
        if file:
            user_directory = os.path.join(settings.MEDIA_ROOT, 'speaking-response', user)
            file_name = f'{exam_id}-{time.strftime("%Y%m%d-%H%M%S")}.{extension}'
            
            os.makedirs(user_directory, exist_ok=True)
            
            file_path = os.path.join(user_directory, file_name)
            return_dir = os.path.join('speaking-response', user, file_name)

            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
                    
            return Response({"file_path": return_dir}, status=200)

        return Response({"msg": "file not found"}, status=200)

class SaveAudio(generics.ListCreateAPIView):
    queryset = SpeakingResponse.objects.all()
    serializer_class = SpeakingAnswerSerializer


class SpeakingAnswerView(generics.CreateAPIView):
    serializer_class = SpeakingAnswerBlockSerializer
    queryset = SpeakingBlockAnswer.objects.all()

class SpeakingPracticeView(APIView):
    queryset = SpeakingBlockAnswer.objects.all()
    serializer_class = SpeakingAnswerBlockSerializer
    
    def get(self, request,id):
        try:
            user = self.request.user.student
        except Exception:
            return Response('Student does not exists')
        try:
            m = module.objects.get(id=id)
        except module.DoesNotExist:
            return Response({'error':'Practice test with this id does not exists'},400)
        res_data = {}
        for speaking_block in m.Speaking.all():
            questions_dict ={}
            for question in speaking_block.questions.all():

                questions_dict[question.question_number] = question.question

            qs = self.queryset.filter(practise_test=m, user=user,Flt__isnull=True,speaking_block=speaking_block)
            
            data = self.serializer_class(qs,many=True, fields=['question_number','answer_audio','user']).data
            print('======================================')
            data = [dict(d) for d in data]
            print('======================================')
            
            for d in data:
                for k,v in questions_dict.items():
                    if d['question_number'] == k:
                        if res_data.get(speaking_block.id,None):
                            res_data[speaking_block.id].append({'question':v,'question_number':k,'answer_audio':d["answer_audio"]})
                        else:
                            res_data[speaking_block.id] = [{'question':v,'question_number':k,'answer_audio':d["answer_audio"]}]
                            
            
        return Response(res_data,200)
        