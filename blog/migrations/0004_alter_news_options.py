# Generated by Django 4.2.6 on 2024-01-12 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_news_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Data', 'verbose_name_plural': 'Products'},
        ),
    ]
