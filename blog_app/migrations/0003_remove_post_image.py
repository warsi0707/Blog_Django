# Generated by Django 4.1.3 on 2023-10-17 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
