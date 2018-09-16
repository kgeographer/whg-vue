from django.conf.urls import url
from backend import views

urlpatterns = [
    url(r'places$', views.place_list),
    url(r'place/(?P<pk>[0-9]+)$', views.place_detail),
]
