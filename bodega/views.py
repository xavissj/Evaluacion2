from django.shortcuts import render
from django.http import HttpResponse
from .models import RegistroProducto
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'bodega/index.html')

@csrf_exempt
def listaProductos(request):
    if request.method == 'GET':
        registros = RegistroProducto.objects.all()
        return render(request, 'bodega/listaProductos.html', {'registros': registros})
    elif request.method == 'POST':
        registro = RegistroProducto()
        registro.nombre = request.POST['nombre']
        registro.fecha = request.POST['fecha']
        registro.cantidad = request.POST['cantidad']
        registro.categoria = request.POST['categoria']
        registro.save()
        return HttpResponse('ok')


def login(request):
    return render(request, 'bodega/login.html')



def registroB(request):
    return render(request, 'bodega/registro-bodeguero.html')


def somos(request):
    return render(request, 'bodega/somos.html')


def contacto(request):
    return render(request, 'bodega/contacto.html')