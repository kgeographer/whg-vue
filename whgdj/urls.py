from django.contrib import admin
from django.urls import path, reverse, include
from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # Vue single page app
    path('', TemplateView.as_view(template_name='whgdj/spa.html'), name='home'),

    # Django
    path('search/', view=TemplateView.as_view(template_name='whgdj/search.html'), name='search'),
    path('blog/', include('blog.urls')),
    path('api/',include('api.urls')),
    path('about/', TemplateView.as_view(template_name='whgdj/about.html'), name='about'),
]
