# Generated by Django 4.2.9 on 2024-03-19 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0005_alter_landingpage_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingpage',
            name='on_air',
            field=models.BooleanField(db_index=True, default=False, help_text='Indica se a página está no ar.'),
        ),
    ]