from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.db.models import Sum
import django_tables2 as tables
import django_filters

from .models import FuncTran
from .forms import FuncTranForm

def cadastrar_funcoes(request):
    submitted = False

    if request.method == "POST":
        form = FuncTranForm(request.POST)
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                param1 = form.cleaned_data['param1']
                param2 = form.cleaned_data['param2']
                tipo_func = form.cleaned_data['tipo_func']
                print(param1, param2, tipo_func)
                instance.compl = calcular_complexidade(int(param2), int(param1))
                print(instance.compl)
                instance.pont_func = calcular_ppf(tipo_func, instance.compl)
                print(instance.pont_func)
                instance.save()
                return HttpResponseRedirect('/?submitted=True')
            except:
                print("porra")
                pass
    else:
        form = FuncTranForm()
        if 'submitted' in request.GET:
                submitted = True

    return render(request,
                  'index.html',
                  {'form': form, 'submitted': submitted})

class SimpleTable(tables.Table):
    class Meta:
        model = FuncTran

# class FuncTranFilter(django_filters.FilterSet):
#     class Meta:
#         model = FuncTran
#         fields = ['tipo_func', 'compl']
#
    # def filter_tipo_func(self, queryset, name, value):
    #     return queryset.filter(**{
    #         name: value,
    #     })

def listar_funcoes(request):

    queryset = FuncTran.objects.all().order_by('tipo_func')
    querysetEE = FuncTran.objects.all().filter(tipo_func='EE')
    querysetSE = FuncTran.objects.all().filter(tipo_func='SE')
    querysetCE = FuncTran.objects.all().filter(tipo_func='CE')
    totalEE = FuncTran.objects.all().filter(tipo_func='EE').aggregate(Sum('pont_func'))
    totalSE = FuncTran.objects.all().filter(tipo_func='SE').aggregate(Sum('pont_func'))
    totalCE = FuncTran.objects.all().filter(tipo_func='CE').aggregate(Sum('pont_func'))
    tableEE = SimpleTable(querysetEE)
    tableSE = SimpleTable(querysetSE)
    tableCE = SimpleTable(querysetCE)

    return render(request, 'list.html', {'tableEE': tableEE, 'tableSE': tableSE, 'tableCE': tableCE, 'totalEE': totalEE['pont_func__sum'], 'totalCE': totalCE['pont_func__sum'], 'totalSE': totalSE['pont_func__sum']})
    # f = FuncTranFilter(request.GET, queryset=FuncTran.objects.all())
    # table = SimpleTable(f)
    #
    # return render(request, 'list.html', {'table': table, 'filter': f})

def calcular_complexidade(alr, der):
    if(alr == 0 or alr == 1):
        if(der >= 1 and der <= 4):
            complexidade = 'B'
        elif(der >= 5 and der <= 15):
            complexidade = 'B'
        elif(der >= 16):
            complexidade = 'M'
    elif(alr == 2):
        if(der >= 1 and der <= 4):
            complexidade = 'B'
        elif(der >= 5 and der <= 15):
            complexidade = 'M'
        elif(der >= 16):
            complexidade = 'A'
    elif(alr > 3):
        if(der >= 1 and der <= 4):
            complexidade = 'M'
        elif(der >= 5 and der <= 15):
            complexidade = 'A'
        elif(der >= 16):
            complexidade = 'A'
    return complexidade


def calcular_ppf(tipo, complexidade):
    if(tipo == 'EE'):
        if(complexidade == 'B'):
            pf = 3
        elif(complexidade == 'M'):
            pf = 4
        elif(complexidade == 'A'):
            pf = 6
    if(tipo == 'SE'):
        if(complexidade == 'B'):
            pf = 4
        elif(complexidade == 'M'):
            pf = 5
        elif(complexidade == 'A'):
            pf = 7
    if(tipo == 'CE'):
        if(complexidade == 'B'):
            pf = 3
        elif(complexidade == 'M'):
            pf = 4
        elif(complexidade == 'A '):
            pf = 6
    return pf
