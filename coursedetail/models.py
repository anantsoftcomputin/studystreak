from ckeditor.fields import RichTextField
# from Courses.models import Course
# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from master.models import Section

# class Lession_Quiz(models.Model):
#     name = models.CharField(max_length=200)
#     
#  = models.ForeignKey("Lesson", on_delete=models.CASCADE, related_name='quizzes')
#     def __str__(self):
#          return f"{self.name}"

# class Question(models.Model):
#     question = models.CharField(max_length=200, null=True, blank=True)
#     quiz = models.ForeignKey("Lesson", on_delete=models.CASCADE, related_name='quizzes')

#     def __str__(self):
#          return f"{self.question}"

# class Lesson(models.Model):
#    # course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, default=None)
#     section = models.ForeignKey(Section,max_length=200, null=True, blank=True, default=None, on_delete=models.CASCADE)
#     Lesson_Title = models.CharField(max_length=200, null=True, blank=True, default=None)
#     Lesson_Description = models.CharField(max_length=200, null=True, blank=True, default=None)
#     Lesson_Video = models.URLField(null=True, blank=True, default=None)
#     Lesson_Duration = models.CharField(max_length=200, null=True, blank=True, default=None)
#     Lesson_attachment = models.FileField(upload_to='documents/', null=True, blank=True, default=None)
#     active = models.BooleanField(default=False)


#     def __str__(self):
#         return self.Lesson_Title

# class Lession_Quiz(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#          return f"{self.name}"

# class Question(models.Model):
#     question = models.CharField(max_length=200, null=True, blank=True)
#     quiz = models.ForeignKey(Lession_Quiz, on_delete=models.CASCADE, related_name='questions')

#     def __str__(self):
#          return f"{self.question}"


class Lesson(models.Model):
    section = models.ForeignKey(
        Section,
        max_length=200,
        null=True,
        blank=True,
        default=None,
        on_delete=models.CASCADE,
    )
    Lesson_Title = models.CharField(max_length=200, default=None)
    Lesson_Description = models.CharField(
        max_length=200, null=True, blank=True, default=None
    )
    Lesson_Video = models.URLField(null=True, blank=True, default=None)
    Lesson_Duration = models.CharField(
        max_length=200, null=True, blank=True, default=None
    )
    active = models.BooleanField(default=False)
    lesson_assignment = models.ManyToManyField('exam.Exam', related_name="lesson_assignment", null=True, blank=True)
    sequence = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return self.Lesson_Title



class QuizOption(models.Model):
    name = models.ForeignKey("Quiz_Question", on_delete=models.CASCADE)
    Answers = models.CharField(max_length=200, null=True, blank=True)
    correct_answer = models.BooleanField(verbose_name="Is this correct?", default=False)

    def __str__(self):
        return str(self.Answers)


class Quiz_Question(models.Model):
    Question = models.CharField(max_length=200, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)  

    def __str__(self):
        return str(self.Question)

    # class Meta:
    #      verbose_name = "L"


    
class Note(models.Model):
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    note = RichTextUploadingField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['student', 'lesson'], name='unique_intro',violation_error_message= "You have already added note for this class"),
    #     ]
          

    def __str__(self):
        return f"{self.student.user.username}"

