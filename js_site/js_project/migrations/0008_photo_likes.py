# Generated by Django 2.0.1 on 2018-01-25 08:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('js_project', '0007_auto_20180125_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
