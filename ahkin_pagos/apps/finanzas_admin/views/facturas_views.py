# Django

from django.shortcuts import render
from django.views.generic.list import View

# models
from ahkin_pagos.apps.finanzas_admin.models import Factura


class FacturasListAdmin(View):
    model = Factura
    template_name = 'facturas_list.html'

    def get_queryset(self):
        queryset = Factura.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        context = {'list_factura': self.get_queryset()}
        return render(request, self.template_name, context)

