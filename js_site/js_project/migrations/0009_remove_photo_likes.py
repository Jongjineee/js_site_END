# Generated by Django 2.0.1 on 2018-01-25 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('js_project', '0008_photo_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='likes',
        ),
    ]
