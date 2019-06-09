from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_funcoes, name='cadastrar_funcoes')
]