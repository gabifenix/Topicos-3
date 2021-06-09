from django.db import models

class cadastro(models.Model):
    nome = models.CharField('Nome',max_length=255)
    idade = models.IntegerField('Idade')
    data = models.IntegerField('Data')
    numero_da_dose = models.IntegerField('Numero da Dose')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    

