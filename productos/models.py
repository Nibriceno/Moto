from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id')
    nombreCategoria = models.CharField(max_length=50,verbose_name='Categoría')
    

    def __str__(self):
        return self.nombreCategoria


class Vehiculo(models.Model):
    patente = models.CharField(max_length=6,primary_key=True, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca')
    Servicio = models.CharField(max_length=20,null=True, blank=True, verbose_name='Servicio')
    modelo = models.CharField(max_length=20,null=True, blank=True, verbose_name='Modelo')
   
    imagen = models.ImageField(upload_to="motocicletas",null=True,blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.patente
    
