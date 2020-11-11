from django.conf.urls import url, include
from ahkin_pagos.apps.custom_user.views import IndexHomeView

urlpatterns = [
    url(r'^$', IndexHomeView.as_view(), name="index_home"),
]
