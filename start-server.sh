#!/usr/bin/env bash
# start-server.sh

USERNAME=admin
EMAIL=admin@myapp.com
PASSWORD=admin

python manage.py makemigrations
python manage.py migrate
#python manage.py createsuperuser
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$USERNAME', '$EMAIL', '$PASSWORD')" | python manage.py shell
python manage.py runserver #0.0.0.0:8000
