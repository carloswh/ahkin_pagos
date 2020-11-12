# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Factura, TipoCambio, Transaction, Articulo, Credito, Pago


class ArticuloInLine(admin.TabularInline):
    model = Articulo
    raw_id_fields = ['factura']
    extra = 0


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado', 'fecha_pago')
    list_select_related = ('forma_pago',)
    raw_id_fields = list_select_related
    search_fields = ('id', 'estado', 'forma_pago')
    inlines = [
        ArticuloInLine
    ]


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('id', 'precio', 'descripcion')
    list_select_related = ('factura',)
    raw_id_fields = list_select_related
    search_fields = ('id',)


@admin.register(TipoCambio)
class TipoCambio(admin.ModelAdmin):
    model = TipoCambio
    list_display = ('nombre', 'valor', 'created')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ('id', 'type_of_transaction', 'factura', 'value', 'regional_value', 'value_charged',
                    'currency', 'rate', 'created_at')
    readonly_fields = ('type_of_transaction', 'factura', 'value', 'regional_value', 'currency',
                       'rate', 'created_at')


class TransactionInline(admin.TabularInline):
    model = Transaction
    readonly_fields = ('id', 'reference', 'type_of_transaction', 'factura', 'value', 'running_balance',
                       'regional_value', 'value_charged', 'currency', 'rate', 'forma_pago', 'created_at')
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Credito)
class CreditoAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado', 'fecha_pago')
    search_fields = ('id', 'estado', 'forma_pago')


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado', 'fecha_pago')
    list_select_related = ('forma_pago',)
    raw_id_fields = list_select_related
    search_fields = ('id', 'estado', 'forma_pago')
