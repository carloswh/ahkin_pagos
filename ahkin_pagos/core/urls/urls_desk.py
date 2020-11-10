"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from django.views.decorators.cache import never_cache

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    url('', include('ahkin_pagos.apps.finanzas_admin.urls')),
    url('', include('ahkin_pagos.apps.custom_user.urls')),
    url('api/', include('ahkin_pagos.core.urls.urls_api')),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
        url('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
