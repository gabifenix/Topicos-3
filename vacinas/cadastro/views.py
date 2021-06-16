from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse 
from .models import Cadastro
from .forms import CadastroForm
from django.contrib import messages

def listaVacinados(request):
    cadastro = Cadastro.objects.all().order_by('-created_at')
    return render(request, 'cadastro/list.html', {'cadastro' : cadastro} )

def cadastroView(request, id):
    cadastro = get_object_or_404(Cadastro, pk=id)
    return render(request, 'cadastro/cadastro.html', {'cadastro' : cadastro})

def novoCadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST) 

        if form.is_valid():
            Cadastro = form.save()
            Cadastro.user = request.user
            Cadastro.save()
            return redirect('/')

    else:
        form = CadastroForm()
        return render(request, 'cadastro/addcadastro.html', {'form': form})

def editCadastro(request, id):
    cadastro = get_object_or_404(Cadastro, pk=id)
    form = CadastroForm(instance=cadastro)

    if(request.method == 'POST'):
        form = CadastroForm(request.POST, instance=cadastro)

        if(form.is_valid()):
            cadastro.save()
            return redirect('/')
        else:
            return render(request, 'cadastro/editcadastro.html', {'form': form, 'cadastro': cadastro})
    else:
        return render(request, 'cadastro/editcadastro.html', {'form': form, 'cadastro': cadastro})

def deleteCadastro(request, id):
    cadastro = get_object_or_404(Cadastro, pk=id)
    cadastro.delete()

    messages.info(request, 'Cadastro deletado com sucesso!')
    
    return redirect('/')

def helloWorld(request):
    return HttpResponse('Hello World!')
