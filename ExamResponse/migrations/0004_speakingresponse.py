# Generated by Django 4.2 on 2024-02-17 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExamResponse', '0003_studentanswer_band'),
    ]

    operations = [
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
