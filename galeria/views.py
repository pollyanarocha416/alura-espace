from galeria.models import Fotografia
from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    fotografias = Fotografia.objects.all()#objtos detro do nosso model
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request):
    return render(request, 'galeria/imagem.html')

