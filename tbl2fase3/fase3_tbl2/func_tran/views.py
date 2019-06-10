from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect

import django_tables2 as tables

from .models import FuncTran
from .forms import FuncTranForm

def cadastrar_funcoes(request):
    submitted = False

    if request.method == "POST":
        form = FuncTranForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/?submitted=True')
            except:
                pass
    else:
        form = FuncTranForm()
        if 'submitted' in request.GET:
                submitted = True

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
                  {'form': form, 'submitted': submitted})

class SimpleTable(tables.Table):
    class Meta:
        model = FuncTran

def listar_funcoes(request):

    # queryset = FuncTran.objects.all().order_by('tipo_func')
    querysetEE = FuncTran.objects.all().filter(tipo_func='EE')
    querysetSE = FuncTran.objects.all().filter(tipo_func='SE')
    querysetCE = FuncTran.objects.all().filter(tipo_func='CE')
    tableEE = SimpleTable(querysetEE)
    tableSE = SimpleTable(querysetSE)
    tableCE = SimpleTable(querysetCE)

    return render(request, 'list.html', {'tableEE': tableEE, 'tableSE': tableSE, 'tableCE': tableCE})
