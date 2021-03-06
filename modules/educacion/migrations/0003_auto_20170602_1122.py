# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-02 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educacion', '0002_auto_20170602_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='categoria',
            field=models.CharField(choices=[('CRE', 'Crédito'), ('APR', 'Ahorro para el retiro'), ('AEI', 'Ahorro e inversión'), ('SEG', 'Seguro'), ('PLA', 'Planeación')], max_length=100),
        ),
        migrations.AlterField(
            model_name='contenido',
            name='tema',
            field=models.CharField(choices=[('MCR', 'Microcréditos'), ('RET', 'Retiro'), ('IDA', 'Instituciones de ahorro'), ('GAH', 'Gasto hormiga'), ('SEG', 'Seguros'), ('MSG', 'Microseguros'), ('BDC', 'Buró de crédito'), ('AHO', 'Ahorro'), ('PRE', 'Presupuesto'), ('FPE', 'Financiamiento para tu empresa'), ('CRE', 'Crédito'), ('SOV', 'Seguro obligatorio vehicular'), ('INV', 'Inversión'), ('IDC', 'Instituciones de crédito')], max_length=100),
        ),
        migrations.AlterField(
            model_name='curso',
            name='categoria',
            field=models.CharField(choices=[('CRE', 'Crédito'), ('APR', 'Ahorro para el retiro'), ('AEI', 'Ahorro e inversión'), ('SEG', 'Seguro'), ('PLA', 'Planeación')], max_length=100),
        ),
    ]
