#!/usr/bin/env bash
# start-server.sh

USERNAME=admin
EMAIL=admin@myapp.com
PASSWORD=admin

export PYTHONPATH="${PYTHONPATH}:$PWD"
python manage.py makemigrations
python manage.py makemigrations feedapp
python manage.py migrate
#python manage.py createsuperuser
# create user is not exist
cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model
User = get_user_model()  # get the currently active user model,
if not User.objects.filter(username="$USERNAME").exists():
    User.objects.create_superuser('$USERNAME', '$EMAIL', '$PASSWORD')
else:
    print('User "{}" exists already'.format("$USERNAME"))
EOF

python manage.py runserver 0.0.0.0:8000
