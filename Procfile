release: python manage.py migrate
release: python manage.py loaddata blog.json
web: gunicorn blog.wsgi:application --log-file -
