release: python manage.py migrate
worker: python manage.py createsuperuser
web: gunicorn blog.wsgi:application --log-file -
