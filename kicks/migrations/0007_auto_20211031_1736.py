# Generated by Django 3.2.8 on 2021-10-31 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kicks', '0006_kicks_sex'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type',
            new_name='Style',
        ),
        migrations.RenameField(
            model_name='kicks',
            old_name='kicks_type',
            new_name='style',
        ),
    ]
