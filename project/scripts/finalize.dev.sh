#!/bin/sh

echo "Running setup script"

python3 manage.py flush --no-input
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createcachetable
python3 manage.py initadmin

echo "Finished setup script"

exec "$@"
