# Generated by Django 4.0.4 on 2022-05-29 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_vehiculo_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='imagen',
            field=models.ImageField(null=True, upload_to='motocicletas'),
        ),
    ]
