# Generated by Django 4.1.1 on 2022-09-09 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_blog_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='slug',
            field=models.SlugField(),
        ),
    ]