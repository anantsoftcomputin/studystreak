# Generated by Django 4.2 on 2024-02-21 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamResponse', '0010_remove_studentanswer_bands'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentanswer',
            name='band',
            field=models.CharField(blank=True, null=True),
        ),
    ]
