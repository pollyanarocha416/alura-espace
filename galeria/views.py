from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Alura Spece</h1><p>Bem vindo ao espaco</p>')

