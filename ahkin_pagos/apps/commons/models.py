# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import uuid


class FormaPago(models.Model):
    MXN = 0
    USD = 1
    MONEDA_EMPRESA = (
        (MXN, 'MXN'),
        (USD, 'USD'),
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100, blank=True)
    visible = models.BooleanField(default=False, verbose_name="Visible para el Cliente", blank=True)
    moneda = models.PositiveSmallIntegerField(choices=MONEDA_EMPRESA, default=USD, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ultima Actualización")

    class Meta:
        verbose_name = "Forma de Pago"
        verbose_name_plural = "Formas de Pago"

    def __unicode__(self):
        return u'{0}'.format(self.nombre)
