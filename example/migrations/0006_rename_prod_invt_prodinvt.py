# Generated by Django 4.1.3 on 2022-11-23 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0005_rename_inventory_prod_invt'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='prod_invt',
            new_name='ProdInvt',
        ),
    ]
