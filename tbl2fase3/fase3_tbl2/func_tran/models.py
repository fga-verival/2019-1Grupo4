from django.db import models
from django.utils import timezone

class FuncTran(models.Model):
    
    TIPO_FUNC = [
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

    nome_func = models.CharField(max_length=64, null=True)

    tipo_func = models.CharField(
        max_length=2,
        choices=TIPO_FUNC,
        default='EE') 

    param1 = models.IntegerField(null=True)

    param2 = models.IntegerField(null=True)

    compl = models.CharField(
        max_length=6,
        choices=COMPLEXIDADE,
        default='B')

    pont_func = models.IntegerField(null=True)

    nome_cont = models.CharField(max_length=128, null=True)
    
    data_cad = models.DateTimeField(default=timezone.now)

