from django.db import models
from django.utils import timezone

class Func_Tran(models.Model):
    
    TIPO_FUNCOES = [
        ('EE', 'Entradas Externas'),
        ('CE', 'Consultas Externas'),
        ('SE', 'Saídas Externas'),
    ]

    COMPLEXIDADE = [
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta'),
    ]

    id = models.AutoField(primary_key=True)

    nome_func = models.CharField(max_length=64)

    tipo_funcoes = models.CharField(
        max_length=2,
        choices=TIPO_FUNCOES,
        default='EE') 

    param1 = models.IntegerField()

    param2 = models.IntegerField()

    compl = models.CharField(
        max_length=6,
        choices=COMPLEXIDADE,
        default='B')

    pont_func = models.IntegerField()

    nome_cont = models.CharField(max_length=128)
    
    data_cad = models.DateTimeField(default=timezone.now)