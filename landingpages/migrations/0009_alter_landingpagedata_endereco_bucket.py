# Generated by Django 4.2.9 on 2024-01-27 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpages', '0008_rename_imagens_links_landingpagedata_nomes_arquivos_imagens_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingpagedata',
            name='endereco_bucket',
            field=models.CharField(blank=True, help_text='https://gjvoxpezczvyqbnmonap.supabase.co/storage/v1/object/public/conecta_bucket/', max_length=200),
        ),
    ]
