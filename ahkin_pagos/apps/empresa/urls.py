from django.conf.urls import url, include

from django.contrib.auth.decorators import login_required
from ahkin_pagos.apps.empresa.views import EmpresasList

urlpatterns = [
    url(r'^empresas/$', login_required(EmpresasList.as_view()), name="lista_empresas"),
]
