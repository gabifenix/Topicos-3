from django.db import models

class Cadastro(models.Model):
    nome = models.CharField('Nome',max_length=255)
    idade = models.CharField('Idade', max_length=255)
    data = models.CharField('Data', max_length=255)
    numero_da_dose = models.CharField('Numero da Dose', max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    

