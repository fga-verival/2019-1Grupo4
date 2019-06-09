from django.db import models
from django.utils import timezone

class Func_Tran(models.Model):
    nome_func = models.CharField(max_length=64)
    tipo_funcoes = models.CharField(max_length=2) ## EE, CE, SE
    param1 = models.IntegerField()
    param2 = models.IntegerField()
    compl = models.CharField(max_length=6) ## baixa, media, alta -> preenchimento pela função
    pont_func = models.IntegerField()
    nome_cont = models.CharField(max_length=128)
    data_cad = models.DateTimeField(default=timezone.now)