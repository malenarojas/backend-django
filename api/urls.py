from rest_framework import routers
router = routers.DefaultRouter()

from django.urls import path,include
from .views import AgenteViewSet,UsuarioViewSet,PropiedadViewSet


router.register('api/agentes',AgenteViewSet)


agente_list = AgenteViewSet.as_view({
    'get': 'list',      # GET /api/agentes/
    'post': 'create'    # POST /api/agentes/
})

agente_detail = AgenteViewSet.as_view({
    'get': 'show',     # GET /api/agentes/<id>/
    'put': 'update',       # PUT /api/agentes/<id>/
    'delete': 'destroy'    # DELETE /api/agentes/<id>/
})
router.register('api/usuarios',UsuarioViewSet)
router.register('api/propiedad',PropiedadViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
