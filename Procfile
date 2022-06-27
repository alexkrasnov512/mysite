release: python manage.py migrate
release: python manage.py createsuperuser
web: gunicorn blog.wsgi:application --log-file -
