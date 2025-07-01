#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations//migro las tablas 
python manage.py migrate

# Load seed data (optional)//lo que contiene las tablas
python manage.py seed_data 