# Generated by Django 3.2.8 on 2021-11-23 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20211113_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='toast_logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='home',
            name='toast_logo_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
