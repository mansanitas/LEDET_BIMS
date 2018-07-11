"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^contact/', include('contactus.urls')),
    url(r'^', include('bims.urls')),
    url(r'^', include('ledet_base.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include(('fish.urls', 'fish'), namespace='fish')),
    url(r'^', include(('reptile.urls', 'reptile'), namespace='reptile')),
]

try:
    from core.urls import urlpatterns as core_urlpatterns
    urlpatterns += core_urlpatterns
except ImportError:
    pass

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )