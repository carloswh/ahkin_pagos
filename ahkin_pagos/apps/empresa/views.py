# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django
from django.shortcuts import render
from django.views.generic.list import View

# Models

from ahkin_pagos.apps.empresa.models import Empresa


class EmpresasList(View):
    model = Empresa
    template_name = 'list_empresas.html'

    def get_queryset(self):
        queryset = Empresa.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        context = {'list_empresa': self.get_queryset(), 'table_name': 'Lista Empresas'}
        return render(request, self.template_name, context)
