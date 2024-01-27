# Generated by Django 4.2.9 on 2024-01-27 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpages', '0005_alter_landingpagedata_imagem_local'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpagedata',
            name='arquivos_local',
            field=models.FileField(blank=True, upload_to='arquivos_teste/'),
        ),
        migrations.AlterField(
            model_name='landingpagedata',
            name='imagem_local',
            field=models.ImageField(blank=True, upload_to='imagens_produtos/'),
        ),
    ]
