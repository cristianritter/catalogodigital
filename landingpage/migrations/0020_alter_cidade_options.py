# Generated by Django 4.2.9 on 2024-02-29 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0019_remove_landingpage_link_loja_empresa_website'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cidade',
            options={'ordering': ['nome'], 'verbose_name': 'Cidade', 'verbose_name_plural': 'Cidades'},
        ),
    ]
