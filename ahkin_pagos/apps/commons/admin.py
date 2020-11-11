# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import FormaPago


@admin.register(FormaPago)
class FormaPagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('id', 'nombre')
