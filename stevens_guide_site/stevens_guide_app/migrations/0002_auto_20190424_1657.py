# Generated by Django 2.2 on 2019-04-24 20:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stevens_guide_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Restaurants',
            new_name='Restaurant',
        ),
    ]
