#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
poetry --version
echo "regenerate poetry.lock"
rm poetry.lock
poetry lock
echo "before install poetry"
poetry install --no-root
pip install --force-reinstall -U setuptools

python manage.py collectstatic --no-input
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.filter(email='y2k2@gmail.com').delete(); User.objects.create_superuser('y2k2@gmail.com', 'y2k2', '1234')" | python manage.py shell