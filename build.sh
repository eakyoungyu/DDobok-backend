#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
echo "update poetry.lock"
poetry lock
poetry update
poetry update --lock
echo "before install poetry"
poetry install
pip install --force-reinstall -U setuptools

python manage.py collectstatic --no-input
python manage.py migrate