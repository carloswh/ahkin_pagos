# Django

from django.shortcuts import render
from django.views.generic.list import View

from ahkin_pagos.apps.finanzas_admin.models import Pago


class PagosListAdmin(View):
    model = Pago
    template_name = 'list_pagos.html'

    def get_queryset(self):
        queryset = Pago.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        context = {'list_pago': self.get_queryset(), 'table_name': 'Tabla Pagos'}
        return render(request, self.template_name, context)
