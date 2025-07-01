"""
Fallback WSGI application for deployment platforms that don't read Procfile correctly.
This imports the Django WSGI application so 'gunicorn app:app' works.
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tecnico_medio.settings')

# Create the WSGI application
app = get_wsgi_application() 