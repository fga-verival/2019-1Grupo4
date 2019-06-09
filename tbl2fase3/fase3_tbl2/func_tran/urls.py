from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostar_cadastro, name='mostrar_cadastro')
]