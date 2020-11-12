# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormView, View

from ahkin_pagos.apps.custom_user.models import User

from ahkin_pagos.apps.custom_user.forms.user_forms import UserForm


class IndexHomeView(View):
    template_name = 'dashboard_finanzas_admin.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class UserLogin(FormView):
    template_name = 'home/index.html'
    form_class = UserForm

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return reverse('index_home')
        else:
            return reverse('login_user')


class ClientesList(View):
    model = User
    template_name = ''

    def get_queryset(self):
        queryset = User.objects.all().exclude(is_staff=True)
        return queryset

    def get(self, request, *args, **kwargs):
        context = {'list_clientes': self.get_queryset(), 'table_name': 'Clientes'}
        return render(request, self.template_name, context)
