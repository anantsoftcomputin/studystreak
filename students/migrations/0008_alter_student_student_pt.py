# Generated by Django 4.2 on 2024-04-16 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Create_Test', '0017_alter_module_practice_test_type'),
        ('students', '0007_alter_student_student_flt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_pt',
            field=models.ManyToManyField(blank=True, null=True, related_name='+', to='Create_Test.createexam'),
        ),
    ]
