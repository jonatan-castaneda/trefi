# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-29 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0004_auto_20170528_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='clase_cuenta',
            field=models.CharField(choices=[('ING', 'Ingreso'), ('GTO', 'Gasto'), ('MTA', 'Meta'), ('EFE', 'Efectivo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='tipo_cuenta',
            field=models.CharField(choices=[('SAL', 'Salario'), ('ALI', 'Alimentos'), ('REN', 'Rendimiento inversiones'), ('OTR', 'Otro'), ('DEP', 'Deporte'), ('HON', 'Honorarios'), ('ACC', 'Accesorios'), ('APU', 'Apuestas'), ('BAN', 'Cuenta Bancaria'), ('AHO', 'Cuenta de Ahorro'), ('ENT', 'Entretenimiento'), ('INV', 'Cuenta de Inversiones'), ('CAR', 'Cartera'), ('TDC', 'Tarjeta de Crédito'), ('VID', 'Videojuegos'), ('NOM', 'Cuenta de Nómina'), ('ROP', 'Ropa')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='clase_trans',
            field=models.CharField(choices=[('ING', 'Ingreso'), ('GTO', 'Gasto'), ('TRA', 'Traspaso')], max_length=100),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='notas',
            field=models.TextField(blank=True, null=True),
        ),
    ]