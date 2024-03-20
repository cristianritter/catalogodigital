# Generated by Django 4.2.9 on 2024-03-19 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0004_alter_landingpage_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingpage',
            name='url',
            field=models.CharField(db_index=True, editable=False, help_text='Endereço de url da página.', max_length=30),
        ),
    ]
