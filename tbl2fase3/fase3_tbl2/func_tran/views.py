from django.shortcuts import render

def mostar_cadastro(request):
    return render(request, 'index.html', {})
