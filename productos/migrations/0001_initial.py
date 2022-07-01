# Generated by Django 4.0.1 on 2022-05-12 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('numrun_cliente', models.IntegerField(primary_key=True, serialize=False, verbose_name='numero de rut del cliente')),
                ('dvrun_cliente', models.IntegerField(max_length=100, verbose_name='digito verificador de rut del cliente')),
                ('nombre_cliente', models.CharField(max_length=100, verbose_name='nombre del cliente')),
                ('appaterno_cliente', models.CharField(max_length=100, verbose_name='apellido paterno del cliente')),
                ('telefono_cliente', models.IntegerField(max_length=100, verbose_name='Telefono del cliente')),
                ('direccion_cliente', models.CharField(max_length=100, verbose_name='Direccion del cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('patente', models.IntegerField(primary_key=True, serialize=False, verbose_name='patente de la moto')),
                ('nombre_marca_moto', models.CharField(max_length=100, verbose_name='Nombre de la Marca de la moto')),
                ('cilindrica', models.IntegerField(max_length=20, verbose_name='cilindrica de la moto')),
                ('precio_moto', models.IntegerField(verbose_name='Valor de la moto')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_Servicio', models.IntegerField(primary_key=True, serialize=False, verbose_name='id del Servicio')),
                ('nombre_Servicio', models.CharField(max_length=100, verbose_name='nombre del Servicio')),
            ],
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id_Servicio', models.IntegerField(primary_key=True, serialize=False, verbose_name='id del tipo del Servicio')),
                ('lavado_moto', models.CharField(max_length=100, verbose_name='Lavado de la moto')),
                ('arreglo_moto', models.CharField(max_length=100, verbose_name='Arreglo de la moto')),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('numrun_vendedor', models.IntegerField(primary_key=True, serialize=False, verbose_name='numero de rut del vendedor')),
                ('dvrun_vendedor', models.IntegerField(max_length=100, verbose_name='digito verificador de rut del vendedor')),
                ('nombre_vendedor', models.CharField(max_length=100, verbose_name='nombre del vendedor')),
                ('appaterno_vendedor', models.CharField(max_length=100, verbose_name='apellido paterno del vendedor')),
                ('telefono_vendedor', models.IntegerField(max_length=100, verbose_name='Telefono del vendedor')),
                ('direccion_vendedor', models.CharField(max_length=100, verbose_name='Direccion del vendedor')),
                ('sueldo_vendedor', models.IntegerField(max_length=100, verbose_name='Sueldo del vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de la venta')),
            ],
        ),
    ]
