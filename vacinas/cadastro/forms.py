from django import forms
from django.forms import fields
from .models import Cadastro

class CadastroForm(forms.ModelForm): 

    class Meta:
        model = Cadastro
        fields = ('nome', 'idade', 'data', 'numero_da_dose')