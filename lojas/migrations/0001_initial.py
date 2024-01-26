# Generated by Django 4.2.9 on 2024-01-26 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LojaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_cadastrado', models.CharField(help_text='O endereço final do link da página', max_length=50)),
                ('caminho_de_arquivos', models.CharField(help_text='cidade/nome_da_empresa', max_length=100)),
                ('meta_description', models.CharField(help_text='Uma descrição que vai aparecer para o usuário durante a busca', max_length=160)),
                ('nome_empresa', models.CharField(help_text='Nome ao lado da logomarca', max_length=30)),
                ('slogam', models.CharField(help_text='Slogam abaixo do nome da empresa', max_length=100)),
                ('titulo', models.CharField(help_text='Tema central na página', max_length=100)),
                ('paragrafo', models.TextField(help_text='Um parágrafo descrevendo a loja', max_length=1000)),
                ('produtos', models.TextField(help_text='Informações do produto passadas no formato Json. Ex:                                \\{                                    "pizza": [                                         ["Pizza de Calabresa", "Calabresa, Queijo Chedar e massa especial", 59.90, "01.jpg"]                                    ]                                }')),
            ],
        ),
    ]
