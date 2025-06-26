from rest_framework import viewsets
from .models import Agente,Usuario, Propiedad, User
from .serializers import AgenteSerilizer, UsuarioSerilizer,PropiedadSerilizer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.core.cache import cache 
from rest_framework.exceptions import AuthenticationFailed
import requests



class AgenteViewSet(viewsets.ModelViewSet):
    queryset = Agente.objects.all()
    serializer_class = AgenteSerilizer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerilizer

class PropiedadViewSet(viewsets.ModelViewSet):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerilizer
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
    
        username = attrs.get("username")

        cache_key = f"login_attempts_{username}"

        attemps = cache.get(cache_key, 0)
        if attemps >= 3:
           raise AuthenticationFailed("Cuenta temporalmente bloqueada por múltiples intentos fallidos.")
        
        try:
            data = super().validate(attrs)
        except AuthenticationFailed:
           cache.set(cache_key,attemps +1, timeout=60*5)
           raise AuthenticationFailed("Credenciales incorrectas. Intento fallido.")
        cache.delete(cache_key)
        # Añadir datos del usuario extra
        user = self.user
        try:
            usuario = Usuario.objects.get(user=user)
            data['user_id'] = user.id
            data['username'] = user.username
            data['email'] = user.email
            data['telefono'] = usuario.telefono
            data['direccion'] = usuario.direccion
        except Usuario.DoesNotExist:
            data['user_id'] = user.id
            data['username'] = user.username
            data['email'] = user.email

        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Sesión cerrada correctamente"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Token inválido o ya fue usado"}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        telefono = data.get("telefono")
        direccion = data.get("direccion")

        if User.objects.filter(username=username).exists():
            return Response({"error": "Nombre de usuario ya existe"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        usuario = Usuario.objects.create(user=user, telefono=telefono, direccion=direccion)

        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "telefono": usuario.telefono,
            "direccion": usuario.direccion
        }, status=status.HTTP_201_CREATED)


class EnviarMensajeWhatsApp(APIView):
    def post(self, request):
        numero_destino = request.data.get("numero")  # formato internacional, ej: 59171234567
        mensaje = request.data.get("mensaje")

        token = "TU_TOKEN_DE_ACCESO"
        telefono_id = "TU_PHONE_NUMBER_ID"

        url = f"https://graph.facebook.com/v19.0/{telefono_id}/messages"

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        data = {
            "messaging_product": "whatsapp",
            "to": numero_destino,
            "type": "text",
            "text": {"body": mensaje},
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            return Response({"detalle": "Mensaje enviado"}, status=status.HTTP_200_OK)
        else:
            return Response(response.json(), status=response.status_code)


