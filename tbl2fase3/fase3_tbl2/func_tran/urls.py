from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_funcoes, name='cadastrar_funcoes'),
    path('list', views.listar_funcoes, name='listar_funcoes')
]
