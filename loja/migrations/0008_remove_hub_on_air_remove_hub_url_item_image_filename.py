# Generated by Django 4.2.9 on 2024-03-15 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0007_remove_hub_nome_remove_hub_slogam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hub',
            name='on_air',
        ),
        migrations.RemoveField(
            model_name='hub',
            name='url',
        ),
        migrations.AddField(
            model_name='item',
            name='image_filename',
            field=models.CharField(blank=True, editable=False, max_length=50),
        ),
    ]
