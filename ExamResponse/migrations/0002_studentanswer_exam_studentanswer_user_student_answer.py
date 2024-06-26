# Generated by Django 4.2 on 2024-02-09 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ExamResponse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentanswer',
            name='exam',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='exam', to='exam.exam'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Student_answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField()),
                ('answer_text', models.TextField()),
                ('student_answers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_exam', to='ExamResponse.studentanswer')),
            ],
        ),
    ]
