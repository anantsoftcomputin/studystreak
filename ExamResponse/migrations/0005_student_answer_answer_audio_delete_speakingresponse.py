# Generated by Django 4.2 on 2024-02-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamResponse', '0004_speakingresponse'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_answer',
            name='answer_audio',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='SpeakingResponse',
        ),
    ]
