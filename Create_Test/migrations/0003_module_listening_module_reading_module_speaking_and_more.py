# Generated by Django 4.2 on 2024-02-08 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam', '0001_initial'),
        ('Create_Test', '0002_createexam_ielts'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='Listening',
            field=models.ManyToManyField(blank=True, null=True, related_name='listening+', to='exam.exam'),
        ),
        migrations.AddField(
            model_name='module',
            name='Reading',
            field=models.ManyToManyField(blank=True, null=True, related_name='reading+', to='exam.exam'),
        ),
        migrations.AddField(
            model_name='module',
            name='Speaking',
            field=models.ManyToManyField(blank=True, null=True, related_name='Speaking+', to='exam.exam'),
        ),
        migrations.AddField(
            model_name='module',
            name='Writing',
            field=models.ManyToManyField(blank=True, null=True, related_name='writing+', to='exam.exam'),
        ),
        migrations.AddField(
            model_name='responses',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.exam'),
        ),
        migrations.AddField(
            model_name='responses',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
