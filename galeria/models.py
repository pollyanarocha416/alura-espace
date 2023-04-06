from django.db import models

# Create your models here.
class Fotografia(models.Model):                         #nignfica vazia
    nome = models.CharField(max_length=100, null=False, blank=False)#vai aceitar caractere
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return f'Fotografia [nome={self.nome}]'
