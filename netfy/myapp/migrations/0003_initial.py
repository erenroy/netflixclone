# Generated by Django 4.2.3 on 2023-10-15 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0002_delete_videodetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
                ('small_image', models.ImageField(upload_to='images')),
                ('big_image', models.ImageField(upload_to='bigimages')),
                ('video_file', models.FileField(upload_to='video')),
            ],
        ),
    ]
