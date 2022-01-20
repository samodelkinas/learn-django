docker-compose run app sh -c "django-admin startproject quiz ."
docker-compose run app sh -c "python manage.py makemigrations && migrate && python manage.py createsuperuser"
