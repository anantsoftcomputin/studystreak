# Generated by Django 4.2 on 2024-04-06 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamResponse', '0030_alter_studentanswer_exam_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentanswer',
            name='band',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
