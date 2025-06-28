# Backend Django - Técnico Medio

Django REST Framework API project with JWT authentication, user management, and property listings.

## Features

- JWT Authentication with login attempt limiting
- User registration and management
- Agent and property management
- WhatsApp integration
- PostgreSQL database support
- API endpoints for CRUD operations

## Local Development

### Prerequisites

- Python 3.12+
- PostgreSQL database
- Virtual environment

### Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd tecnico-medio-django/tecnico_medio
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requeriments.txt
```

4. Create `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

5. Configure your environment variables in `.env`:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

6. Run migrations:
```bash
python manage.py migrate
```

7. Create superuser (optional):
```bash
python manage.py createsuperuser
```

8. Load seed data (optional):
```bash
python manage.py seed_data
```

9. Run development server:
```bash
python manage.py runserver
```

## Deployment on Render

### Quick Deploy

1. Fork this repository to your GitHub account

2. Connect your GitHub repository to Render

3. Choose "Web Service" and configure:
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn tecnico_medio.wsgi:application`
   - **Python Version**: 3.12

### Environment Variables on Render

Set these environment variables in your Render dashboard:

```
SECRET_KEY=<generate-a-secure-secret-key>
DEBUG=False
DATABASE_URL=<your-postgresql-database-url>
ALLOWED_HOSTS=<your-render-app-name>.onrender.com
```

### Database Setup

1. Create a PostgreSQL database on Render
2. Copy the DATABASE_URL from your database dashboard
3. Add it to your web service environment variables

### Automatic Deployment

If you included the `render.yaml` file, Render will automatically:
- Create the web service
- Create a PostgreSQL database
- Set up the necessary environment variables

## API Endpoints

### Authentication
- `POST /api/auth/login/` - Login with username/password
- `POST /api/auth/logout/` - Logout (blacklist token)
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/refresh/` - Refresh JWT token

### Users & Agents
- `GET /api/usuarios/` - List users
- `POST /api/usuarios/` - Create user
- `GET/PUT/DELETE /api/usuarios/{id}/` - User details

- `GET /api/agentes/` - List agents
- `POST /api/agentes/` - Create agent
- `GET/PUT/DELETE /api/agentes/{id}/` - Agent details

### Properties
- `GET /api/propiedades/` - List properties
- `POST /api/propiedades/` - Create property
- `GET/PUT/DELETE /api/propiedades/{id}/` - Property details

### Utilities
- `POST /api/whatsapp/` - Send WhatsApp message

## Project Structure

```
tecnico_medio/
├── api/                    # Main API app
│   ├── models.py          # Database models
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views
│   ├── urls.py            # URL routing
│   └── management/        # Custom commands
├── tecnico_medio/         # Project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL config
│   └── wsgi.py            # WSGI application
├── build.sh               # Render build script
├── Procfile               # Process file for deployment
├── render.yaml            # Render service configuration
├── runtime.txt            # Python version specification
└── requeriments.txt       # Python dependencies
```

## Technologies Used

- **Backend**: Django 5.0, Django REST Framework
- **Authentication**: JWT (Simple JWT)
- **Database**: PostgreSQL
- **Deployment**: Render
- **Additional**: WhatsApp API integration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for educational purposes.
