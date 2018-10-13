from django.conf.urls import url
from backend import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'places', views.PlaceList.as_view()),
    url(r'places/(?P<pk>[0-9]+)$', views.PlaceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
