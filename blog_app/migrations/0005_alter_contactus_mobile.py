# Generated by Django 4.1.3 on 2023-10-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='mobile',
            field=models.IntegerField(max_length=20),
        ),
    ]