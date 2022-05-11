import imp
from django.conf import settings
from django.urls import path
from . import views
# for downloading files
from django.conf.urls.static import static
from django.conf import settings

# IVOSHET: added + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# for url to static files and downloading
# urlpatterns = [
#     path('', views.game_list, name='game_list'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('game/<int:pk>/', views.game_detail, name='game_detail')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
