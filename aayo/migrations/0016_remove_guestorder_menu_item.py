# Generated by Django 5.0.7 on 2024-08-06 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aayo', '0015_rename_menu_name_guestorder_menu_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestorder',
            name='menu_item',
        ),
    ]
