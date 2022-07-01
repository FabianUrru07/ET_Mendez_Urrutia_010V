from django.db import models

# Create your models here.

class Producto(models.Model):
    idProducto = models.CharField(max_length=6, primary_key=True, verbose_name='Id')
    nombre= models.CharField(max_length=20, verbose_name='Nombre')
    precio=models.CharField(max_length=20, verbose_name='Precio')
    descripcion=models.CharField(max_length=100,verbose_name='Descripcion',null=True)
    imagen=models.ImageField(upload_to='static/img/',verbose_name='Imagen')    

    def __str__(self):
        return self.idProducto

class Cliente(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, verbose_name='Rut')
    nombre= models.CharField(max_length=20, verbose_name='Nombre', null=True)
    direccion=models.CharField(max_length=20, verbose_name='Direccion', null=True)
    email=models.CharField(max_length=20, verbose_name='Email', null=True)
    telefono=models.CharField(max_length=20, verbose_name='Telefono', null=True)

    def __str__(self):
        return self.rut