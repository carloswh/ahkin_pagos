# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-11-10 21:32
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0001_initial'),
        ('finanzas_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('descripcion', models.TextField(blank=True)),
                ('cantidad', models.PositiveSmallIntegerField(default=1)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_extra', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de Creaci\xf3n')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articulos', to='finanzas_admin.Factura')),
            ],
            options={
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos',
            },
        ),
        migrations.CreateModel(
            name='TipoCambio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('nombre', models.CharField(max_length=40)),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Tipo de cambio',
                'verbose_name_plural': 'Tipo de cambio',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('value', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=8, verbose_name='Monto Transacci\xf3n')),
                ('value_charged', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=15, verbose_name='Total Cobrado')),
                ('regional_value', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=8, verbose_name='Monto Origen')),
                ('currency', models.PositiveSmallIntegerField(choices=[(1, 'USD'), (2, 'MEX'), (3, 'COP'), (4, 'EUR'), (5, 'PEN'), (6, 'GTQ')], editable=False, verbose_name='Divisa Origen')),
                ('rate', models.DecimalField(decimal_places=2, editable=False, max_digits=8, verbose_name='Tipo de cambio')),
                ('running_balance', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=8, verbose_name='Balance Actual')),
                ('type_of_transaction', models.SmallIntegerField(choices=[(1, 'ABONO'), (2, 'CARGO'), (3, 'TRANSFERENCIA')], editable=False, verbose_name='Tipo de Transacci\xf3n')),
                ('description', models.TextField(blank=True, editable=False, null=True, verbose_name='Descripci\xf3n')),
                ('reference', models.CharField(blank=True, editable=False, max_length=50, null=True, verbose_name='Referencia')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')),
                ('fecha_pago', models.DateTimeField(blank=True, null=True)),
                ('factura', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions_factura', to='finanzas_admin.Factura')),
                ('forma_pago', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='forma_pago_transactions', to='commons.FormaPago', verbose_name='Forma de Pago')),
            ],
        ),
    ]