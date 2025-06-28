#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requeriments.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Load seed data (optional)
python manage.py seed_data 