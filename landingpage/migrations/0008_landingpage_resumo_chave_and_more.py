# Generated by Django 4.2.9 on 2024-02-09 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0007_alter_landingpage_link_loja'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='resumo_chave',
            field=models.TextField(default=1, help_text='Este resumo é o cabeçalho h2 de sua página. Deve ser uma descrição bem clara e objetiva e obrigatóriamente conter as palavras chaves de pesquisa.', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='lista_items',
            field=models.TextField(blank=True, help_text='Itens da lista em formato de list ["abc", "cde"]', max_length=600),
        ),
    ]