django-migrate:
	uv run ./manage.py migrate

start:
	uv run ./manage.py runserver

admin:
	DJANGO_SUPERUSER_USERNAME=admin \
	DJANGO_SUPERUSER_PASSWORD=111 \
	DJANGO_SUPERUSER_EMAIL=admin@emorozov.net \
	uv run ./manage.py createsuperuser --name='Eugene Morozov' --noinput || true


make-trans:
	django-admin makemessages -l ru -e py -i venv

compile-trans:
	django-admin compilemessages --exclude venv

start-mailhog:
	docker run -d --rm --name mailhog -p 127.0.0.1:1025:1025 -p 127.0.0.1:8025:8025 mailhog/mailhog:v1.0.1

