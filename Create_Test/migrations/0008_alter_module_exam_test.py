# Generated by Django 4.2 on 2024-02-27 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Create_Test', '0007_alter_module_exam_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='exam_test',
            field=models.CharField(blank=True, choices=[('Practice', 'Practice'), ('Full Length', 'Full Length')], max_length=20, null=True),
        ),
    ]
