from django.db import models

class cadastroModel(models.Model):
    nome = models.CharField('Nome',max_length=50)
    idade = models.IntegerField('Idade')
    data = models.IntegerField('Data')
    numero_da_dose = models.IntegerField('Número da dose')

    def __str__(self):
        return self.nome