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
        data = super().validate(attrs)

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





