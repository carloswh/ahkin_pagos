# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ahkin_pagos.apps.empresa.models import Empresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    model = Empresa
    list_display = ('nombre', 'slug', 'email', 'created',)
    list_select_related = ()
    raw_id_fields = list_select_related
    search_fields = ('nombre', 'slug',)
