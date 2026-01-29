#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

cd ecommerce_api

python manage.py collectstatic --noinput
python manage.py migrate

python manage.py createsuperuser --noinput || true
