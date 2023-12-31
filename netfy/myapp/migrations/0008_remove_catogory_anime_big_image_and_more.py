# Generated by Django 4.2.3 on 2023-10-18 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_catogory_anime_catogory_movie_catogory_new_release'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catogory_anime',
            name='big_image',
        ),
        migrations.RemoveField(
            model_name='catogory_anime',
            name='date',
        ),
        migrations.RemoveField(
            model_name='catogory_anime',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='catogory_anime',
            name='video_file',
        ),
        migrations.RemoveField(
            model_name='catogory_movie',
            name='big_image',
        ),
        migrations.RemoveField(
            model_name='catogory_movie',
            name='date',
        ),
        migrations.RemoveField(
            model_name='catogory_movie',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='catogory_movie',
            name='video_file',
        ),
        migrations.RemoveField(
            model_name='catogory_new_release',
            name='big_image',
        ),
        migrations.RemoveField(
            model_name='catogory_new_release',
            name='date',
        ),
        migrations.RemoveField(
            model_name='catogory_new_release',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='catogory_new_release',
            name='video_file',
        ),
        migrations.AlterField(
            model_name='catogory_anime',
            name='small_image',
            field=models.ImageField(upload_to='animme_images'),
        ),
        migrations.AlterField(
            model_name='catogory_movie',
            name='small_image',
            field=models.ImageField(upload_to='movie_images'),
        ),
        migrations.AlterField(
            model_name='catogory_new_release',
            name='small_image',
            field=models.ImageField(upload_to='new_images'),
        ),
    ]
