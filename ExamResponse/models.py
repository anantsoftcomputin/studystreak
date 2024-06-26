from django.contrib.auth.models import User
from django.db import models

from Create_Test.models import FullLengthTest, module
# Create your models here.
# Test
from exam.models import Exam, ExamType, SpeakingBlock


class Studentanswer(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    exam = models.ForeignKey(Exam, related_name="exam", on_delete=models.CASCADE, null=True, blank=True)
    Practise_Exam = models.ForeignKey(module, on_delete=models.CASCADE, null=True, blank=True)
    Full_Length_Exam = models.ForeignKey(FullLengthTest, on_delete=models.CASCADE, null=True, blank=True, related_name = "full_length+")
    AI_Assessment = models.TextField(null=True, blank=True)
    Tutor_Assessment = models.TextField(null=True, blank=True)
    band = models.CharField(max_length = 50, null=True, blank=True)
    exam_type = models.CharField(max_length=30, choices = ExamType.choices, null=True, blank=True)
    speaking_block = models.ForeignKey(SpeakingBlock,on_delete=models.CASCADE,null=True,blank=True)
class Student_answer(models.Model):
    student_answers = models.ForeignKey(
        Studentanswer, related_name="student_exam", on_delete=models.CASCADE
    )
    question_number = models.IntegerField()
    answer_text = models.TextField(blank=True, null=True)
    


class SpeakingResponse(models.Model):
    student_answers = models.ForeignKey(Studentanswer, on_delete=models.CASCADE, related_name="student_exams")
    question_number = models.IntegerField()
    answer_audio = models.FileField(upload_to='speaking-response/')


class SpeakingBlockAnswer(models.Model):
    user = models.ForeignKey('students.Student',on_delete=models.CASCADE,)
    
    practise_test = models.ForeignKey(module, on_delete=models.CASCADE, null=True, blank=True)
    speaking_block = models.ForeignKey('exam.SpeakingBlock',on_delete=models.CASCADE, verbose_name='speakng block',related_name='answers')
    Flt = models.ForeignKey(FullLengthTest, on_delete=models.CASCADE, null=True, blank=True, related_name = "full_length+")
    AI_Assessment = models.TextField(null=True, blank=True)
    Tutor_Assessment = models.TextField(null=True, blank=True)
    band = models.CharField(max_length = 50, null=True, blank=True)
    question_number = models.IntegerField()
    answer_audio = models.FileField(upload_to='speaking-response/')
    

    class Meta:
        verbose_name =  "Speaking Block Answer"
    