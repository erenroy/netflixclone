# Generated by Django 4.2.3 on 2023-10-22 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_delete_usermovieinteraction'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='user_image',
            field=models.ImageField(default=None, upload_to='user_profile_images'),
        ),
    ]
