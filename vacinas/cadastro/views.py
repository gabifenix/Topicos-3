from django.shortcuts import render
from django.http import HttpResponse 

from .models import cadastro

def listaVacinados(request):
     
    return render(request, 'cadastro/list.html', {'cadastro' : cadastro} )


