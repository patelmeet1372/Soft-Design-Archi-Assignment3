# Generated by Django 4.1.3 on 2022-11-23 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0003_inventory_bar_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='item_name',
            new_name='item_bc',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='item_price',
            new_name='item_details',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='bar_code',
        ),
    ]