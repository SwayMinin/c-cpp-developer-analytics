from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('demand', views.demand, name='demand'),
    path('geography', views.geography, name='geography'),
    path('skills', views.skills, name='skills'),
    path('latest', views.latest, name='latest'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
