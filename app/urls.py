from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:tema>/<int:id_prod>/', views.producto, name='producto'),
    path('<str:tema>/', views.temas, name='temas'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)