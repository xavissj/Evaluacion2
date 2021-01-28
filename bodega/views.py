from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'bodega/index.html')

def listaProductos(request):
    return render(request, 'bodega/listaProductos.html')

def login(request):
    return render(request, 'bodega/login.html')

def registroB(request):
    return render(request, 'bodega/registro-bodeguero.html')

def somos(request):
    return render(request, 'bodega/somos.html')

def contacto(request):
    return render(request, 'bodega/contacto.html')