# Generated by Django 3.2.8 on 2021-11-21 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_rename_user_profile_order_user_orders_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_orders_profile',
            new_name='user_profile',
        ),
    ]
