# Generated by Django 4.2 on 2024-04-09 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LiveClass', '0009_liveclassattachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='liveclassattachment',
            name='file_name',
            field=models.CharField(default=1),
            preserve_default=False,
        ),
    ]
