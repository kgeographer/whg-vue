from django.contrib import admin
from django.urls import path, reverse, include
from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    # Django
    path('admin', admin.site.urls),
    url(r'^api/', include('backend.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),

    # catchall to Vue single page app
    url(r'^.*$', TemplateView.as_view(template_name='whgdj/spa.html'), name='home'),
]
