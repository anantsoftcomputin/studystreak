# Generated by Django 4.2 on 2024-03-17 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursedetail', '0005_rename_live_class_note_lesson'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='note',
            name='unique_intro',
        ),
        migrations.AddConstraint(
            model_name='note',
            constraint=models.UniqueConstraint(fields=('student', 'lesson'), name='unique_intro', violation_error_message='You have already added note for this class'),
        ),
    ]
