# Generated by Django 4.2 on 2024-02-21 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamResponse', '0007_studentanswer_gpt_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentanswer',
            name='band',
            field=models.CharField(blank=True, null=True),
        ),
    ]
