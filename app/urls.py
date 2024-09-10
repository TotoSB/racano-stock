from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:tema>/<int:id_prod>/', views.producto, name='producto'),
    path('<str:tema>/<int:id_prod>/<int:id_variante>/', views.variante, name='variante'),
    path('editar_modelo/<int:id_modelo>/', views.editar_producto_variante, name='editar_var'),
    path('<str:tema>/', views.temas, name='temas'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)