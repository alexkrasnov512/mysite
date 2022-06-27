release: python manage.py migrate
release: python manage.py createsuperuser --noinput --username "root" --email "orelkiller7@gmail.com" --password "12345"
web: gunicorn blog.wsgi:application --log-file -
