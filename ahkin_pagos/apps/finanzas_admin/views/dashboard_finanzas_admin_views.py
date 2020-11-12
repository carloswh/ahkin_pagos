from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def admin_finance_panel(request):
    return render(request, 'dashboard_finanzas_admin.html')
