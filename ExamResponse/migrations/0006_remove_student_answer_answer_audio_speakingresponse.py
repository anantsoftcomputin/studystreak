# Generated by Django 4.2 on 2024-02-17 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExamResponse', '0005_student_answer_answer_audio_delete_speakingresponse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_answer',
            name='answer_audio',
        ),
        migrations.CreateModel(
            name='SpeakingResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField()),
                ('answer_audio', models.FileField(upload_to='')),
                ('student_answers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExamResponse.studentanswer')),
            ],
        ),
    ]
