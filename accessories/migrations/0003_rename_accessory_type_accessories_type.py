# Generated by Django 3.2.8 on 2021-11-05 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accessories', '0002_auto_20211028_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessories',
            old_name='accessory_type',
            new_name='type',
        ),
    ]
