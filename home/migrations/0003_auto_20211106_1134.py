# Generated by Django 3.2.8 on 2021-11-06 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211106_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='friendly_name',
        ),
        migrations.RemoveField(
            model_name='discount',
            name='name',
        ),
        migrations.RemoveField(
            model_name='home',
            name='friendly_name',
        ),
        migrations.RemoveField(
            model_name='home',
            name='name',
        ),
    ]