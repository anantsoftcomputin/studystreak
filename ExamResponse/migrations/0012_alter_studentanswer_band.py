# Generated by Django 4.2 on 2024-02-21 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamResponse', '0011_studentanswer_band'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentanswer',
            name='band',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
