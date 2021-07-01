# Generated by Django 3.2.4 on 2021-07-01 03:28

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/header_image'),
        ),
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='coding', max_length=225),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=225),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/profile_pics')),
                ('website_url', models.CharField(blank=True, max_length=250, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=250, null=True)),
                ('github_url', models.CharField(blank=True, max_length=250, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=250, null=True)),
                ('dribble_url', models.CharField(blank=True, max_length=250, null=True)),
                ('figma_url', models.CharField(blank=True, max_length=250, null=True)),
                ('codepen_url', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
