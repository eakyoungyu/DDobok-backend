#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
poetry update --lock
poetry install
pip install --force-reinstall -U setuptools

python manage.py collectstatic --no-input
python manage.py migrate