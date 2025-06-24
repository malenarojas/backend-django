from rest_framework import routers

from django.urls import path
from .views import CustomTokenObtainPairView
from django.urls import path,include
from .views import AgenteViewSet,UsuarioViewSet,PropiedadViewSet, LogoutView, RegisterView
router = routers.DefaultRouter()

router.register('api/agentes',AgenteViewSet)
router.register('api/usuarios',UsuarioViewSet)
router.register('api/propiedad',PropiedadViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/register/', RegisterView.as_view(), name='register'),
]
