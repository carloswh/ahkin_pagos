# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import JSONField

import uuid

CURRENCY_STORE_FIELD = getattr(settings, 'TRANSACTION_CURRENCY_STORE_FIELD', models.DecimalField)
User = get_user_model()


class Factura(models.Model):
    PENDIENTE = 0
    PAGADA = 1
    PARCIAL = 2
    CANCELADA = 3
    REVISION = 3
    ESTADO_FACTURA = (
        (PENDIENTE, 'Pendiente de pago'),
        (PAGADA, 'Pagada'),
        (PARCIAL, 'Parcialidad'),
        (CANCELADA, 'Cancelada'),
        (REVISION, 'En Revision'),
    )
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    fecha_pago = models.DateTimeField()
    estado = models.PositiveSmallIntegerField(choices=ESTADO_FACTURA, default=PENDIENTE, db_index=True)
    tipo_cambio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    comision = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    impuestos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_impuestos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(default=0, verbose_name="Balance", max_digits=8, decimal_places=2, blank=True,
                                  help_text="Balance a Favor el valor es Negativo, Saldo Pendiente el valor Positivo")
    balance_nuevo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, default=0,
                                        verbose_name="Saldo Nuevo a Favor", help_text="Saldo a Favor el valor es \
                                        Negativo, Saldo Pendiente el valor Positivo")

    total = models.DecimalField(max_digits=10, decimal_places=2)
    total_mxn = models.DecimalField(max_digits=10, decimal_places=2)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    referencia = models.CharField(max_length=100, verbose_name="Referencia de pago", blank=True)
    reporto_cliente = models.BooleanField(default=False)
    forma_pago = models.ForeignKey('commons.FormaPago', related_name="forma_pago_factura", blank=True, null=True)
    cajero = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="cajero_factura", null=True, blank=True)
    cliente = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="cliente_factura", null=True,
                                verbose_name="Usuario asignado")

    def __unicode__(self):
        return u'{0}'.format(self.id)


class Transaction(models.Model):

    TYPE = (
        (1, 'ABONO'),
        (2, 'CARGO'),
        (3, 'TRANSFERENCIA'),
    )
    CURRENCIES = (
        (1, 'USD'),
        (2, 'MEX'),
        (3, 'COP'),
        (4, 'EUR'),
        (5, 'PEN'),
        (6, 'GTQ'),
    )

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    value = CURRENCY_STORE_FIELD(verbose_name='Monto Transacción', default=0, max_digits=8,
                                 decimal_places=2, editable=False)
    value_charged = CURRENCY_STORE_FIELD(verbose_name='Total Cobrado', max_digits=15, decimal_places=2, default=0,
                                         editable=False)
    regional_value = CURRENCY_STORE_FIELD(verbose_name='Monto Origen', default=0,
                                          max_digits=8, decimal_places=2, editable=False)
    currency = models.PositiveSmallIntegerField(verbose_name='Divisa Origen', choices=CURRENCIES, editable=False)
    rate = CURRENCY_STORE_FIELD('Tipo de cambio', max_digits=8, decimal_places=2, editable=False)
    running_balance = CURRENCY_STORE_FIELD("Balance Actual", default=0, max_digits=8, decimal_places=2, editable=False)
    type_of_transaction = models.SmallIntegerField(choices=TYPE, verbose_name="Tipo de Transacción", editable=False)
    description = models.TextField(null=True, blank=True, verbose_name="Descripción", editable=False)
    reference = models.CharField(max_length=50, blank=True, null=True, verbose_name="Referencia", editable=False)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro', editable=False)
    fecha_pago = models.DateTimeField(blank=True, null=True)

    factura = models.ForeignKey('finanzas_admin.Factura', on_delete=models.CASCADE,
                                related_name='transactions_factura', null=True, editable=False)

    forma_pago = models.ForeignKey("commons.FormaPago", verbose_name="Forma de Pago", on_delete=models.SET_NULL,
                                   null=True, editable=False, related_name="forma_pago_transactions")

    def __unicode__(self):
        return u'{0} - {1} - {2}'.format(self.get_type_of_transaction_display(), self.get_currency_display(),
                                         self.wallet)


class Articulo(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    descripcion = models.TextField(blank=True)
    cantidad = models.PositiveSmallIntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    factura = models.ForeignKey('finanzas_admin.Factura', related_name="articulos", on_delete=models.CASCADE)
    data_extra = JSONField(blank=True, null=True)
    created = models.DateField(auto_now_add=True, editable=False, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    def __unicode__(self):
        return u'{0}'.format(self.id)


class TipoCambio(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    nombre = models.CharField(max_length=40)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Tipo de cambio"
        verbose_name_plural = "Tipo de cambio"

    def __str__(self):
        return u"{0}={1}".format(self.nombre, self.valor)


class Pago(models.Model):
    SIN_FACTURAR = 0
    FACTURADO = 1
    CANCELADO = 2
    PARCIAL = 3
    ESTADO_PAGO = (
        (SIN_FACTURAR, 'Sin facturar'),
        (FACTURADO, 'Facturado'),
        (CANCELADO, 'Cancelado'),
        (PARCIAL, 'Parcial')
    )
    CARGO = 0
    ABONO = 1
    TIPO_PAGO = (
        (CARGO, 'Cargo'),
        (ABONO, 'Abono')
    )
    CURRENCIES = (
        (1, 'USD'),
        (2, 'MEX'),
        (3, 'COP'),
        (4, 'EUR'),
        (5, 'PEN'),
        (6, 'GTQ'),
    )
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    fecha_pago = models.DateField()
    estado = models.PositiveSmallIntegerField(choices=ESTADO_PAGO, default=SIN_FACTURAR, db_index=True)
    tipo_pago = models.PositiveSmallIntegerField(choices=TIPO_PAGO, default=CARGO, db_index=True)
    tipo_cambio = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.PositiveSmallIntegerField(verbose_name='Divisa Origen', choices=CURRENCIES, editable=False)
    detalles = models.TextField(null=True, blank=True, verbose_name="Detalles", editable=False)
    created = models.DateField(auto_now_add=True, editable=False, verbose_name="Fecha de Creación")

    total = models.DecimalField(max_digits=10, decimal_places=2)
    total_mxn = models.DecimalField(max_digits=10, decimal_places=2)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    residuo = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    forma_pago = models.ForeignKey("commons.FormaPago", verbose_name="Forma de Pago", on_delete=models.SET_NULL,
                                   null=True, editable=False, related_name="forma_pago_pagos")
    factura = models.ForeignKey('finanzas_admin.Factura', on_delete=models.CASCADE,
                                related_name='pago_factura', null=True, editable=False)
    facturas_aplicadas = models.ManyToManyField('finanzas_admin.Factura', blank=True)
    cliente = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="cliente_pago", null=True,
                                verbose_name="Usuario asignado")
