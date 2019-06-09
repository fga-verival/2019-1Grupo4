from django.shortcuts import render
from django.utils import timezone

from .models import FuncTran

def cadastrar_funcoes(request):

    form = FuncTran()

    # form.nome_func = request.POST['nome_func']
    # form.tipo_func = request.POST['tipo_func']
    # form.param1 = request.POST['param1']
    # form.param2 = request.POST['param2']
    # form.compl = request.POST['compl']
    # form.pont_func = request.POST['pont_func']
    # form.nome_cont = request.POST['nome_cont']
    # form.data_cad = timezone.now()

    # form.save()

    #func_trans = Func_Tran.objects.filter()
    return render(request,
                  'index.html',
                  {})
