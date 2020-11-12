# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_countries.fields import CountryField


class Empresa(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    descripcion = models.TextField(max_length=200, blank=True)
    direccion = models.TextField(max_length=100, blank=True)
    coordenadas = models.CharField(max_length=80, blank=True, verbose_name="Coordenadas")
    telefono = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True, )
    pagina_web = models.URLField(max_length=150, blank=True)
    rfc = models.CharField(max_length=30, blank=True, verbose_name="RFC/RUC")
    rfc_sat = models.CharField(max_length=30, blank=True, null=True, default="", verbose_name="RFC SAT")
    direccion_facturacion = models.TextField(max_length=100, blank=True)
    pais = CountryField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    ultimo_acceso = models.DateTimeField(null=True, blank=True)
    facturas_pagadas = models.BooleanField(default=True, verbose_name="¿Ha pagado todas sus facturas?")
    saldo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, help_text="Saldo a Favor si es negativo, Saldo Pendiente si positivo", default=0)

    def __unicode__(self):
        return u'{0}'.format(self.nombre)
