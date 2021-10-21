# Generated by Django 3.2.8 on 2021-10-21 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kicks', '0003_kicks_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kicks',
            old_name='image',
            new_name='default_image',
        ),
        migrations.AddField(
            model_name='kicks',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='kicks',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='kicks',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]