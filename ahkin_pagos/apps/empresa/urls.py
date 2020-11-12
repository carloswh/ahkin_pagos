from django.conf.urls import url, include

from django.contrib.auth.decorators import login_required
from ahkin_pagos.apps.empresa.views import EmpresasList, EmpresaCreateForm

urlpatterns = [
    url(r'^registro-empresa/$', EmpresaCreateForm.as_view(), name="registro-empresa"),
    url(r'^empresas/$', login_required(EmpresasList.as_view()), name="lista_empresas"),
    url(r'^accounts/', include('allauth.urls')),
]
