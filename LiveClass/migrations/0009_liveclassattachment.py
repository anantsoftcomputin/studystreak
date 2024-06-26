# Generated by Django 4.2 on 2024-04-09 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LiveClass', '0008_delete_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveClassAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(upload_to='liveclass/%y/%m/%d')),
                ('live_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LiveClass.live_class')),
            ],
        ),
    ]
