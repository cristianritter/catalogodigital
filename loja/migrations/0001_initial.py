# Generated by Django 4.2.9 on 2024-03-21 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('landingpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_air', models.BooleanField(db_index=True, default=False, help_text='Indica se a página está no ar.')),
                ('url', models.CharField(db_index=True, editable=False, help_text='Endereço de url da página.', max_length=30)),
                ('titulo', models.CharField(help_text='Tema central na página', max_length=100)),
                ('paragrafo', models.TextField(help_text='Parágrafo de boas vindas', max_length=600)),
                ('produtos', models.TextField(help_text='Informações do produto passadas no formato Json. Ex: {"pizza": ["Pizza de Calabresa", "Calabresa, Queijo Chedar e massa especial", 59.90, "nome_do_arquivo"]}')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landingpage.empresa')),
            ],
            options={
                'verbose_name': '   Store',
                'verbose_name_plural': '   Stores',
            },
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.store')),
            ],
            options={
                'verbose_name': '  Shelf',
                'verbose_name_plural': '  Shelves',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('imagem_url', models.CharField(blank=True, max_length=255, null=True)),
                ('image_filename', models.CharField(blank=True, editable=False, max_length=50)),
                ('shelf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loja.shelf')),
            ],
            options={
                'verbose_name': ' Item',
                'verbose_name_plural': ' Items',
            },
        ),
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_air', models.BooleanField(db_index=True, default=False, help_text='Indica se a página está no ar.')),
                ('url', models.CharField(db_index=True, editable=False, help_text='Endereço de url da página.', max_length=30)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landingpage.empresa')),
                ('lojas', models.ManyToManyField(to='loja.store')),
            ],
            options={
                'verbose_name': 'Concentrador',
                'verbose_name_plural': 'Concentradores',
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
