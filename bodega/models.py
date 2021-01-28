from django.db import models

class RegistroProducto(models.Model):
    sku = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    fecha = models.CharField(max_length=8)
    cantidad = models.IntegerField()
    categoria = models.IntegerField()
