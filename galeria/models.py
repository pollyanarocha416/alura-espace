from datetime import datetime
from django.db import models

# Create your models here.
class Fotografia(models.Model):           
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]              #nignfica vazia
    nome = models.CharField(max_length=100, null=False, blank=False)#vai aceitar caractere
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateField(default=datetime.now, blank=False)


    def __str__(self) -> str:
        return self.nome
