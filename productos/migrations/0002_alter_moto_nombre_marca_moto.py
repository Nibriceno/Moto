# Generated by Django 4.0.1 on 2022-05-12 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moto',
            name='nombre_marca_moto',
            field=models.CharField(max_length=100, verbose_name='Marca'),
        ),
    ]