from django.urls import path
from . import views

urlpatterns = [
    path('', views.libro_lista, name='libro_lista'),
    path('libro/<int:pk>/', views.libro_detalle, name='libro_detalle'),
    path('libro/nuevo/', views.libro_nuevo, name='libro_nuevo'),
    path('libro/<int:pk>/editar/', views.libro_editar, name='libro_editar'),
    path('libro/<int:pk>/eliminar/', views.libro_eliminar, name='libro_eliminar'),
]
