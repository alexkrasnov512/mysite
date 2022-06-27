export DJANGO_SUPERUSER_USERNAME = root
export DJANGO_SUPERUSER_EMAIL = test@test.com
export DJANGO_SUPERUSER_PASSWORD = 12345
release: python manage.py migrate
release: python manage.py createsuperuser --noinput
web: gunicorn blog.wsgi:application --log-file -
