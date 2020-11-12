from django.conf.urls import url, include

from django.contrib.auth.decorators import login_required
from ahkin_pagos.apps.custom_user.views import IndexHomeView, UserLogin

urlpatterns = [
    url(r'^home/$', login_required(IndexHomeView.as_view()), name="index_home"),
    url(r'^$', UserLogin.as_view(), name="login_user"),
]
