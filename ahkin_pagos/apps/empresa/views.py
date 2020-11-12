# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import View

# Models

from ahkin_pagos.apps.empresa.models import Empresa

# Forms
from ahkin_pagos.apps.empresa.forms import NewSignUpForm


class EmpresaCreateForm(CreateView):
    template_name = 'signup.html'
    form_class = NewSignUpForm
    model = Empresa

    def get_success_url(self):
        estatus = "created"
        messages.success(self.request, "<i class='fa fa-check'></i> Se ha creado la empresa correctamente")
        return reverse('login_user')


class EmpresasList(View):
    model = Empresa
    template_name = 'list_empresas.html'

    def get_queryset(self):
        queryset = Empresa.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        context = {'list_empresa': self.get_queryset(), 'table_name': 'Lista Empresas'}
        return render(request, self.template_name, context)
