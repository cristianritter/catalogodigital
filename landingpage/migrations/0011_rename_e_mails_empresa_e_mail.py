# Generated by Django 4.2.9 on 2024-02-25 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0010_rename_categoriaservico_categoria_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='e_mails',
            new_name='e_mail',
        ),
    ]
