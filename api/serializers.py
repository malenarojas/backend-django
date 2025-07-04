from rest_framework import serializers
from .models import Agente
from .models import Propiedad
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields =[
            'id',
            'user',
            'telefono',
            'direccion'
        ]

class AgenteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Agente 
        fields =[
            'id',
            'nombre',
            'correo',
            'telefono'
        ]
        
class PropiedadSerializer(serializers.ModelSerializer):
     agente = serializers.PrimaryKeyRelatedField(queryset=Agente.objects.all(), write_only=True)
     propietario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), write_only=True)
     class Meta:
        model= Propiedad 
        fields =[
            'id',
            'titulo',
            'descripcion',
            'precio',
            'agente',
            'propietario',
        ]