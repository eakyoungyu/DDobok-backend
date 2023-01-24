#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
poetry --version
echo "update poetry"
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 - --uninstall
curl -sSL https://install.python-poetry.org | python3 -
# poetry self update
# echo "update poetry.lock"
# poetry lock
echo "before install poetry"
poetry install
pip install --force-reinstall -U setuptools

python manage.py collectstatic --no-input
python manage.py migrate