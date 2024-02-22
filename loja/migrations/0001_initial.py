# Generated by Django 4.2.9 on 2024-02-22 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_air', models.BooleanField(default=False, help_text='Indica se a página está no ar.')),
                ('url', models.CharField(help_text='A parte personalizada do endereço no final do link da página', max_length=50)),
                ('link_whats', models.URLField(blank=True, help_text='https://api.whatsapp.com/send?phone=')),
                ('link_facebook', models.URLField(blank=True, help_text='Link para a página do facebook')),
                ('link_instagram', models.URLField(blank=True, help_text='Link para a página do instagram')),
                ('nome_empresa', models.CharField(help_text='Nome da empresa, da loja ou do concentrador', max_length=50)),
                ('redes_sociais', models.TextField(blank=True, help_text='Links das redes sociais separados por linha', max_length=500)),
                ('slogam', models.CharField(help_text='Slogam abaixo do nome da empresa', max_length=100)),
                ('titulo', models.CharField(help_text='Tema central na página', max_length=100)),
                ('paragrafo', models.TextField(help_text='Um parágrafo descrevendo a loja', max_length=1000)),
                ('produtos', models.TextField(help_text='Informações do produto passadas no formato Json. Ex: {"pizza": ["Pizza de Calabresa", "Calabresa, Queijo Chedar e massa especial", 59.90, "nome_do_arquivo"]}')),
            ],
            options={
                'verbose_name': 'Registro de Loja',
                'verbose_name_plural': 'Registros de Lojas',
            },
        ),
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_air', models.BooleanField(default=False, help_text='Indica se a página está no ar.')),
                ('url', models.CharField(help_text='A parte personalizada do endereço no final do link da página', max_length=50)),
                ('link_whats', models.URLField(blank=True, help_text='https://api.whatsapp.com/send?phone=')),
                ('link_facebook', models.URLField(blank=True, help_text='Link para a página do facebook')),
                ('link_instagram', models.URLField(blank=True, help_text='Link para a página do instagram')),
                ('nome_empresa', models.CharField(help_text='Nome da empresa, da loja ou do concentrador', max_length=50)),
                ('redes_sociais', models.TextField(blank=True, help_text='Links das redes sociais separados por linha', max_length=500)),
                ('nome', models.CharField(help_text='Nome do Food Park centralizador', max_length=100)),
                ('slogam', models.CharField(help_text='Slogam do Food Park centralizador', max_length=100)),
                ('lojas', models.ManyToManyField(to='loja.loja')),
            ],
            options={
                'verbose_name': 'Registro de Hub',
                'verbose_name_plural': 'Registros de Hubs',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.item')),
            ],
        ),
    ]
