from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to="media")
    nombre = models.CharField(max_length=40)
    precio_proveedor = models.IntegerField(default=0)
    precio_unidad = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=200)
    creacion = models.DateField(auto_now_add=True)


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(default=0)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class ventas(models.Model):
    id = models.AutoField(primary_key=True)
    valor_venta = models.IntegerField(default=0)
    
    
    