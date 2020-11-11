# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import View

from ahkin_pagos.apps.custom_user.models import User


class IndexHomeView(View):
    template_name = 'dashboard_finanzas_admin.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ClientesList(View):
    model = User
    template_name = ''

    def get_queryset(self):
        queryset = User.objects.all().exclude(is_staff=True)
        return queryset

    def get(self, request, *args, **kwargs):
        context = {'list_clientes': self.get_queryset(), 'table_name': 'Clientes'}
        return render(request, self.template_name, context)
