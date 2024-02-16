# Generated by Django 4.2.9 on 2024-02-15 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0010_alter_landingpage_gmaps_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='trend_words',
            field=models.CharField(default=1, help_text='Palavras chaves consultadas no Google Trend', max_length=300),
            preserve_default=False,
        ),
    ]