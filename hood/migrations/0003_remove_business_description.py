# Generated by Django 3.1.2 on 2020-10-27 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_remove_profile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='description',
        ),
    ]