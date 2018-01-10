"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
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
from django.conf.urls import url, include
from django.contrib import admin
from landing import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^about/$', views.landing, name='landing'),
    url(r'^novinky/$', views.novinky, name='novinky'),
    url(r'^sunglasses/$', views.sunglasses, name='sunglasses'),
    url(r'^gotmetall/$', views.gotmetall, name='gotmetall'),
    url(r'^gotplastik/$', views.gotplastik, name='gotplastik'),
    url(r'^vfutlyare/$', views.vfutlyare, name='vfutlyare'),
    url(r'^gotdetplastik/$', views.gotdetplastik, name='gotdetplastik'),
    url(r'^antifari/$', views.antifari, name='antifari'),
    url(r'^bezopr/$', views.bezopr, name='bezopr'),
    url(r'^taktik/$', views.taktik, name='taktik'),
    url(r'^trenag/$', views.trenag, name='trenag'),
    url(r'^komp/$', views.komp, name='komp'),
    url(r'^izum/$', views.izum, name='izum'),
    url(r'^lektor/$', views.lektor, name='lektor'),
    url(r'^linzy/$', views.linzy, name='linzy'),
    url(r'^futlar/$', views.futlar, name='futlar'),
    url(r'^metall/$', views.metall, name='metall'),
    url(r'^plastik/$', views.plastik, name='plastik'),
    url(r'^odetmetall/$', views.odetmetall, name='odetmetall'),
]
