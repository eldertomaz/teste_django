#!/bin/sh
set -e

while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
  echo "Banco de dados $DATABASE_HOST:$DATABASE_PORT..."
  sleep 1
done

python manage.py makemigrations app --no-input
python manage.py migrate --no-input

python manage.py collectstatic --no-input


python3 manage.py runserver #0.0.0.0:8000

