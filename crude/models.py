from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=20,null=False)
    apellido=models.TextField(max_length=20,null=False)
    correo = models.EmailField(max_length=30, unique=True)
    telefono = models.CharField(max_length=20,null=True)

    def __str__(self):
        fila=f"Nombre: {self.nombre} {self.apellido}"
        return fila

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, null=False)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=100)


