# Generated by Django 4.2.9 on 2024-03-01 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_alter_item_shelf_to'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='shelf_to',
            new_name='shelf',
        ),
    ]
