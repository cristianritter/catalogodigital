python manage.py compress --force
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
heroku logs --tail -a catalogodigital
heroku domains:add ajrcutelaria.mk4digital.com -a catalogodigital
pip freeze > .\requirements.txt
heroku logs --tail -a catalogodigital  
pip install -r .\requirements.txt
heroku run python manage.py createsuperuser -a catalogodigital