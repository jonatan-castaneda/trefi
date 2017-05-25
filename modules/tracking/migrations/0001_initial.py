# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-25 01:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CuentaEfectivo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_cuenta', models.CharField(choices=[('CAR', 'Cartera'), ('OTR', 'Otro'), ('AHO', 'Cuenta de Ahorro'), ('TDC', 'Tarjeta de Crédito'), ('NOM', 'Cuenta de Nómina'), ('BAN', 'Cuenta Bancaria'), ('INV', 'Cuenta de Inversiones')], max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('presupuesto', models.DecimalField(decimal_places=2, max_digits=9)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=9)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CuentaGasto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_cuenta', models.CharField(choices=[('DEP', 'Deporte'), ('ALI', 'Alimentos'), ('ACC', 'Accesorios'), ('ROP', 'Ropa'), ('VID', 'Videojuegos'), ('ENT', 'Entretenimiento')], max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('presupuesto', models.DecimalField(decimal_places=2, max_digits=9)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=9)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CuentaIngreso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_cuenta', models.CharField(choices=[('SAL', 'Salario'), ('HON', 'Honorarios'), ('REN', 'Rendimiento inversiones'), ('APU', 'Apuestas')], max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('presupuesto', models.DecimalField(decimal_places=2, max_digits=9)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=9)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=9)),
                ('fecha', models.DateField(null=True)),
                ('notas', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('a_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking.CuentaGasto')),
                ('de_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking.CuentaEfectivo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=9)),
                ('fecha', models.DateField(null=True)),
                ('notas', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('a_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking.CuentaEfectivo')),
                ('de_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking.CuentaIngreso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
