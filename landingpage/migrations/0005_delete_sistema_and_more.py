# Generated by Django 4.2.9 on 2024-02-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0004_remove_landingpage_endereco_bucket'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sistema',
        ),
        migrations.RemoveField(
            model_name='landingpage',
            name='nomes_arquivos_imagens',
        ),
        migrations.RemoveField(
            model_name='landingpage',
            name='url_cadastrado',
        ),
        migrations.AddField(
            model_name='landingpage',
            name='carousel_size',
            field=models.IntegerField(default=1, help_text='Quantidade de imagens no carossel da página.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landingpage',
            name='url',
            field=models.CharField(default='teste', help_text='A parte personalizada do endereço no final do link da página', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='link_facebook',
            field=models.URLField(blank=True, help_text='Link para a página do facebook'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='link_instagram',
            field=models.URLField(blank=True, help_text='Link para a página do instagram'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='link_loja',
            field=models.URLField(blank=True, help_text='Link para loja virtual'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='link_whats',
            field=models.URLField(blank=True, help_text='https://api.whatsapp.com/send?phone=5199876543'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='meta_description',
            field=models.CharField(blank=True, help_text='Descrição do site que vai aparecer para o usuário durante a busca.', max_length=160),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='nome_empresa',
            field=models.CharField(help_text='Nome da empresa, da loja ou do concentrador', max_length=50),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='reviews_link',
            field=models.URLField(blank=True, help_text='Link para os reviews do google'),
        ),
    ]