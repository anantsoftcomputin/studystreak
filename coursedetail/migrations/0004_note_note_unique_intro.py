# Generated by Django 4.2 on 2024-03-17 14:39

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_alter_student_student_mock'),
        ('coursedetail', '0003_lesson_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('live_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coursedetail.lesson')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
        migrations.AddConstraint(
            model_name='note',
            constraint=models.UniqueConstraint(fields=('student', 'live_class'), name='unique_intro', violation_error_message='You have already added note for this class'),
        ),
    ]