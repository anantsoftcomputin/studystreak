# Generated by Django 4.2 on 2024-02-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamResponse', '0012_alter_studentanswer_band'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentanswer',
            name='band',
            field=models.CharField(blank=True, null=True),
        ),
    ]
