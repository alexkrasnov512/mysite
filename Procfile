release: python manage.py migrate
release: python manage.py createsuperuser2 --username root --password 123321 --noinput --email 'blank@email.com'
web: gunicorn blog.wsgi:application --log-file -
