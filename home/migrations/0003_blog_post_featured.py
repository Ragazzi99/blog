# Generated by Django 4.1.1 on 2022-09-06 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blog_post_mostviewed_blog_post_newpost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]
