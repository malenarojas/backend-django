from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import Agente, Usuario, Propiedad
from decimal import Decimal


class Command(BaseCommand):
    help = 'Seed database with sample data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--mode',
            type=str,
            help='Mode: refresh, clear',
            default='refresh'
        )

    def handle(self, *args, **options):
        mode = options['mode']
        
        if mode == 'clear':
            self.clear_data()
        elif mode == 'refresh':
            self.clear_data()
            self.create_sample_data()
        else:
            self.create_sample_data()

    def clear_data(self):
        """Clear all existing data"""
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        
        Propiedad.objects.all().delete()
        Usuario.objects.all().delete()
        Agente.objects.all().delete()
        # Only delete non-superuser users
        User.objects.filter(is_superuser=False).delete()
        
        self.stdout.write(self.style.SUCCESS('Data cleared successfully!'))

    def create_sample_data(self):
        """Create sample data"""
        self.stdout.write(self.style.SUCCESS('Creating sample data...'))
        
        # Create sample Agentes
        agentes_data = [
            {
                'nombre': 'Carlos Rodriguez',
                'correo': 'carlos.rodriguez@realestate.com',
                'telefono': '+56987654321'
            },
            {
                'nombre': 'Maria Gonzalez',
                'correo': 'maria.gonzalez@realestate.com',
                'telefono': '+56912345678'
            },
            {
                'nombre': 'Juan Perez',
                'correo': 'juan.perez@realestate.com',
                'telefono': '+56998765432'
            },
            {
                'nombre': 'Ana Martinez',
                'correo': 'ana.martinez@realestate.com',
                'telefono': '+56955443322'
            }
        ]

        agentes = []
        for agente_data in agentes_data:
            agente = Agente.objects.create(**agente_data)
            agentes.append(agente)
            self.stdout.write(f'Created Agente: {agente.nombre}')

        # Create sample Users and Usuarios
        usuarios_data = [
            {
                'username': 'juanlopez',
                'email': 'juan.lopez@email.com',
                'password': 'password123',
                'telefono': '+56977888999',
                'direccion': 'Av. Principal 123, Santiago'
            },
            {
                'username': 'mariasoto',
                'email': 'maria.soto@email.com',
                'password': 'password123',
                'telefono': '+56966777888',
                'direccion': 'Calle Los Alamos 456, Valparaiso'
            },
            {
                'username': 'pedrocastillo',
                'email': 'pedro.castillo@email.com',
                'password': 'password123',
                'telefono': '+56955666777',
                'direccion': 'Pasaje Las Flores 789, Concepcion'
            },
            {
                'username': 'luisamedina',
                'email': 'luisa.medina@email.com',
                'password': 'password123',
                'telefono': '+56944555666',
                'direccion': 'Av. Libertad 321, La Serena'
            }
        ]

        usuarios = []
        for usuario_data in usuarios_data:
            # Create Django User
            user = User.objects.create_user(
                username=usuario_data['username'],
                email=usuario_data['email'],
                password=usuario_data['password']
            )
            
            # Create Usuario profile
            usuario = Usuario.objects.create(
                user=user,
                telefono=usuario_data['telefono'],
                direccion=usuario_data['direccion']
            )
            usuarios.append(usuario)
            self.stdout.write(f'Created Usuario: {usuario.user.username}')

        # Create sample Propiedades
        propiedades_data = [
            {
                'titulo': 'Casa Moderna en Las Condes',
                'descripcion': 'Hermosa casa de 3 dormitorios con jardin y estacionamiento.',
                'precio': Decimal('250000000.00'),  # 250 million CLP
            },
            {
                'titulo': 'Apartamento Luminoso Centro',
                'descripcion': 'Departamento de 2 dormitorios en el centro de Santiago.',
                'precio': Decimal('120000000.00'),  # 120 million CLP
            },
            {
                'titulo': 'Casa Familiar en Providencia',
                'descripcion': 'Amplia casa familiar con 4 dormitorios y patio.',
                'precio': Decimal('180000000.00'),  # 180 million CLP
            },
            {
                'titulo': 'Penthouse Vista al Mar',
                'descripcion': 'Lujoso penthouse con vista al oceano en Viña del Mar.',
                'precio': Decimal('450000000.00'),  # 450 million CLP
            },
            {
                'titulo': 'Casa de Campo',
                'descripcion': 'Encantadora casa rural con terreno amplio.',
                'precio': Decimal('95000000.00'),   # 95 million CLP
            },
            {
                'titulo': 'Departamento Nuevo en Ñuñoa',
                'descripcion': 'Moderno departamento de 1 dormitorio, recien construido.',
                'precio': Decimal('85000000.00'),   # 85 million CLP
            }
        ]

        for i, propiedad_data in enumerate(propiedades_data):
            propiedad = Propiedad.objects.create(
                titulo=propiedad_data['titulo'],
                descripcion=propiedad_data['descripcion'],
                precio=propiedad_data['precio'],
                agente=agentes[i % len(agentes)],  # Distribute properties among agents
                propietario=usuarios[i % len(usuarios)]  # Distribute properties among users
            )
            self.stdout.write(f'Created Propiedad: {propiedad.titulo}')

        # Summary
        self.stdout.write(
            self.style.SUCCESS(
                f'\nSeeding completed successfully!\n'
                f'Created {len(agentes)} Agentes\n'
                f'Created {len(usuarios)} Usuarios\n'
                f'Created {len(propiedades_data)} Propiedades'
            )
        ) 