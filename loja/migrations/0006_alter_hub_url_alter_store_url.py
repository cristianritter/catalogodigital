# Generated by Django 4.2.9 on 2024-03-13 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0005_hub_url_store_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hub',
            name='url',
            field=models.CharField(editable=False, help_text='Endereço de url da página.', max_length=30),
        ),
        migrations.AlterField(
            model_name='store',
            name='url',
            field=models.CharField(editable=False, help_text='Endereço de url da página.', max_length=30),
        ),
    ]
