# Generated by Django 3.2.8 on 2021-11-22 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kicks', '0007_auto_20211031_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kicks',
            name='sizes_available',
        ),
        migrations.AlterField(
            model_name='kicks',
            name='sku',
            field=models.CharField(max_length=254),
        ),
    ]
