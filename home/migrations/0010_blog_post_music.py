# Generated by Django 4.1.1 on 2022-09-12 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_blog_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='music',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]