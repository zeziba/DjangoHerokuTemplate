#!/bin/bash
exec docker-compose run --rm web sh -c "while ! nc -w 1 -z db 5432; do sleep 1; done; ./manage.py test $@"