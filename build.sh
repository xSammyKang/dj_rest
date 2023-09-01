#!/usr/bin/env bash

set -o errexit  # exit on error

pip install django
pip install djangorestframework
pip install gunicorn
pip install djoser
pip install django-cors-headers
pip install whitenoise

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate