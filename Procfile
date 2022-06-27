release: python manage.py migrate
release: python manage.py createsuperuser --no-input --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL --password $DJANGO_SUPERUSER_PASSWORD
web: gunicorn blog.wsgi:application --log-file -
