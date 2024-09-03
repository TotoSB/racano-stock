from django.db import models
from colorfield.fields import ColorField

# Create your models here.

class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to="media")
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True)
    creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Producto_modelo(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.TextField(max_length=100)
    descripcion = models.TextField()
    color = ColorField(default='#FF0000')
    precio_proveedor = models.IntegerField(default=0)
    precio_unidad = models.IntegerField(default=0)

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(default=0)
    producto = models.ForeignKey(Producto_modelo, on_delete=models.CASCADE)

class Ventas(models.Model):
    id = models.AutoField(primary_key=True)
    valor_venta = models.IntegerField(default=0)