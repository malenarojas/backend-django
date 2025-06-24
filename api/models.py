from django.db import models
from django.contrib.auth.models import User


class Agente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    
    def __srt__(self):
        return self.nombre
    

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    telefono = models.CharField(max_length=20)
    direccion =models.CharField(max_length=200)
    def __str__(self):
        return self.user.username
    
class Propiedad(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, related_name='propiedades')
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='propiedades')
    def __str__(self):
        return self.titulo
    

        
