clean:
	find .name "*.pyc" --delete

deps:
	pip install -r requirements.txt

setup:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py createsuperuser --username "admin" --email "hello@wavez.com.br"

run:
	python manage.py runserver