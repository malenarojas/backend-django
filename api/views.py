from django.shortcuts import render
from rest_framework import viewsets
from .models import Agente,Usuario, Propiedad
from .serializers import AgenteSerilizer, UsuarioSerilizer,PropiedadSerilizer


class AgenteViewSet(viewsets.ModelViewSet):
    queryset = Agente.objects.all()
    serializer_class = AgenteSerilizer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerilizer


class PropiedadViewSet(viewsets.ModelViewSet):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerilizer
