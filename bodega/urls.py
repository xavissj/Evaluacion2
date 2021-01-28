from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.listaProductos, name='listaProductos'),
    path('login/', views.login, name= 'login'),
    path('registrob/', views.registroB, name='registrob'),
    path('somos/', views.somos, name='somos'),
    path('contacto/', views.contacto, name='contacto'),
]