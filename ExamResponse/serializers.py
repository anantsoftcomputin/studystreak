from rest_framework import serializers

from .models import SpeakingResponse, Student_answer, Studentanswer


class StudentAnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student_answer
        fields = ("id", "question_number", "answer_text")
        depth = 2

    # def get_student_answers(self, obj):
    #     student_answers = Student_answer.objects.filter(student_exam=obj)
    #     return StudentAnswerAnswerSerializers(student_answers, many=True).data


# class StudentAnswerAnswerSerializers(serializers.ModelSerializer):
#     # student_exam = StudentAnswerSerializers(many=True)
#     student_answers = serializers.SerializerMethodField()

#     class Meta:
#         model = Studentanswer
#         # fields = "__all__"
#         fields = ("id", "user", "exam", "student_answers")
#         depth = 2

#     # def create(self, validated_data):
#     #     answers_data = validated_data.pop("student_exam")
#     #     data = super().create(validated_data)
#     #     if answers_data is not None:
#     #         for answer_data in answers_data:
#     #             Student_answer.objects.create(student_answers=data, **answer_data)
#     #     return data

#     def get_student_answers(self, obj):
#         student_answers = Student_answer.objects.filter(student_exam=obj)
#         serialized_answers = StudentAnswerAnswerSerializers(student_answers, many=True).data
#         return serialized_answers


class SpeakingAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakingResponse
        fields = "__all__"


class StudentanswerSerializers(serializers.ModelSerializer):
    student_exam = StudentAnswerSerializers(many=True, required=False)
    speaking_data = SpeakingAnswerSerializer(many=True, required=False)

    class Meta:
        model = Studentanswer
        fields = (
            "id",
            "user",
            "exam",
            "student_exam",
            "speaking_data",
        )

    def create(self, validated_data):
        studentanswer = Studentanswer.objects.create(**validated_data)

        student_exam_data = validated_data.pop("student_exam", None)
        speaking_data = validated_data.pop("speaking_data", None)

        if speaking_data:
            for speaking_answer_data in speaking_data:
                SpeakingResponse.objects.create(
                    student_answers=studentanswer, **speaking_answer_data
                )

        if student_exam_data:
            for answer_data in student_exam_data:
                Student_answer.objects.create(
                    student_answers=studentanswer, **answer_data
                )

        return studentanswer
