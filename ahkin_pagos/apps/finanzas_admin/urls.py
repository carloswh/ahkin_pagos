from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from ahkin_pagos.apps.finanzas_admin.views.dashboard_finanzas_admin_views import admin_finance_panel
from ahkin_pagos.apps.finanzas_admin.views.facturas_views import FacturasListAdmin

urlpatterns = [
    #Dashboard
    url(r'^panel_home_admin/$', login_required(admin_finance_panel), name="panel_home_admin"),

    # Facturas
    url(r'^facturas/$', login_required(FacturasListAdmin.as_view()), name="lista_facturas"),
]
