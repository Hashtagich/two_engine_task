#!/bin/sh

# Apply database migrations
cd "$(dirname "$0")/task_management"
echo "Applying database migrations"
python manage.py makemigrations
python manage.py migrate

# Create superuser if not already exists
echo "Creating superuser"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

# Launch Gunicorn
echo "Starting Gunicorn"
exec gunicorn task_management.wsgi:application --bind 0.0.0.0:8000 --log-level info
