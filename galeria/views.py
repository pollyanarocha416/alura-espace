from galeria.models import Fotografia
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse



def index(request):
    fotografias = Fotografia.objects.all()#objtos detro do nosso model
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia =  get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})
