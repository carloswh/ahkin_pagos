# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-11-11 14:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finanzas_admin', '0002_articulo_tipocambio_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_emision', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
                ('fecha_pago', models.DateField()),
                ('estado', models.PositiveSmallIntegerField(choices=[(0, 'Sin facturar'), (1, 'Facturado'), (2, 'Cancelado'), (3, 'Parcial')], db_index=True, default=0)),
                ('tipo_pago', models.PositiveSmallIntegerField(choices=[(0, 'Cargo'), (1, 'Abono')], db_index=True, default=0)),
                ('tipo_cambio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.PositiveSmallIntegerField(choices=[(1, 'USD'), (2, 'MEX'), (3, 'COP'), (4, 'EUR'), (5, 'PEN'), (6, 'GTQ')], editable=False, verbose_name='Divisa Origen')),
                ('detalles', models.TextField(blank=True, editable=False, null=True, verbose_name='Detalles')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de Creaci\xf3n')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_mxn', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_pagado', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('residuo', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cliente_pago', to=settings.AUTH_USER_MODEL, verbose_name='Usuario asignado')),
                ('factura', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pago_factura', to='finanzas_admin.Factura')),
                ('facturas_aplicadas', models.ManyToManyField(blank=True, to='finanzas_admin.Factura')),
                ('forma_pago', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='forma_pago_pagos', to='commons.FormaPago', verbose_name='Forma de Pago')),
            ],
        ),
    ]