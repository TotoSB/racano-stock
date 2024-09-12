from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_modelo/<int:id_modelo>/', views.crear_variante, name="crear_mod"),
    path('crear_producto/<int:id_tema>/', views.crear_producto, name="crear_prod"),
    path('editar_modelo/<int:id_modelo>/', views.editar_producto_variante, name='editar_var'),
    path('editar_producto/<int:id_prod>/', views.editar_producto, name='editar_producto'),
    path('producto/<str:tema>/<int:id_prod>/', views.producto, name='producto'),
    path('producto/<str:tema>/<int:id_prod>/<int:id_variante>/', views.variante, name='variante'),
    path('categoria/<str:tema>/', views.temas, name='temas'),
    path('eliminar_producto/<int:id_prod>/', views.eliminar_producto, name='eliminar_producto'),
    path('eliminar_variante/<int:id_variante>/', views.eliminar_variante, name='eliminar_variante'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)