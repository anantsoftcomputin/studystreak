# Generated by Django 4.2 on 2024-02-08 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coursedetail', '0002_lesson_lesson_assignment'),
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='section',
            field=models.ForeignKey(blank=True, default=None, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.section'),
        ),
    ]
