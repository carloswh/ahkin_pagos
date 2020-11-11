# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import View


class IndexHomeView(View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        print('sssss')
        return render(request, self.template_name)
