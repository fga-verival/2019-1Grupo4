from django import forms
from func_tran.models import Func_Tran

class CreateFuncTranForm(forms.ModelForm):
    nome_func = forms.CharField(
        error_messages={
            'required': 'O nome da funcionalidade é obrigatório'}
    )
    tipo_funcoes = forms.CharField(
        error_messages={
            'required': 'O tipo da funcionalidade é obrigatório'}
    )
    param1 = forms.IntegerField(
        error_messages={
            'required': 'O parâmetro 1 é obrigatório'}
    )

    param2 = forms.IntegerField(
        error_messages={
            'required': 'O parâmetro 2 é obrigatório'}
    )

    nome_cont = forms.CharField(
        error_messages={
            'required': 'O nome do contador é obrigatório'}
    )

    class Meta():
        model = Func_Tran
        fields = ('nome_func', 'tipo_funcoes', 'param1', 'param2', 'nome_cont')
