# Generated by Django 4.1.5 on 2023-01-16 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '상품', 'verbose_name_plural': '상품(들)'},
        ),
    ]
