# Generated by Django 4.2.9 on 2024-01-29 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco_bucket', models.CharField(help_text='https://gjvoxpezczvyqbnmonap.supabase.co/storage/v1/object/public/conecta_bucket/', max_length=200)),
                ('on_air', models.BooleanField(help_text='Indica se a página está no ar.')),
                ('url_cadastrado', models.CharField(help_text='O endereço final do link da página', max_length=50)),
                ('nome_empresa', models.CharField(help_text='Servirá como título da Página', max_length=50)),
                ('link_whats', models.URLField(blank=True, help_text='https://api.whatsapp.com/send?phone=SEU_NUMERO_DE_TELEFONE')),
                ('link_instagram', models.URLField(blank=True)),
                ('link_facebook', models.URLField(blank=True)),
                ('meta_description', models.CharField(help_text='Uma descrição que vai aparecer para o usuário durante a busca', max_length=160)),
                ('slogam', models.CharField(help_text='Slogam abaixo do nome da empresa', max_length=100)),
                ('titulo', models.CharField(help_text='Tema central na página', max_length=100)),
                ('paragrafo', models.TextField(help_text='Um parágrafo descrevendo a loja', max_length=1000)),
                ('produtos', models.TextField(help_text='Informações do produto passadas no formato Json. Ex:                                {"pizza": [["Pizza de Calabresa", "Calabresa, Queijo Chedar e massa especial", 59.90, "01.jpg"]\\]}')),
            ],
            options={
                'verbose_name': 'Registro de Loja',
                'verbose_name_plural': 'Registros de Lojas',
            },
        ),
    ]
