# Generated by Django 4.2.9 on 2024-03-21 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0004_alter_landingpage_heading_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingpage',
            name='heading_style',
            field=models.IntegerField(choices=[(0, 'Dark'), (1, 'Light'), (2, 'Texto sobre a imagem'), (3, 'Texto na imagem')], default=0),
        ),
    ]
