# Generated by Django 4.2 on 2024-03-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamResponse', '0018_alter_speakingresponse_student_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speakingresponse',
            name='answer_audio',
            field=models.FileField(),
        ),
    ]
