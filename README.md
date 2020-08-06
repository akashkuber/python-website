python-django-app
Download latest python

Download python IDE pycharm to code in python

set python env using following command or using pycharm create new project it will automatically create venv for you

$ python3 -m venv website

Activate Env
$ source pyShop/bin/activate

check Env
$ which python

open project code in pycharm IDE and run following command

$ pip install django==2.1.5

create django project
$ django-admin startproject websitw

to run project
$ python3 manage.py runserver

to create new app inside pyShop
$ python3 manage.py startapp TechnicalCourses

create migration
$ python3 manage.py makemigrations

migrate the project database
$ python3 manage.py migrate.

run python project
$ python3 manage.py runserver

createsuperuser
$ python manage.py createsuperuser

Username: demo Email address: demo@demo.com

Password: ********** Password (again): ********* Superuser created successfully.

open following into browser

http://127.0.0.1:8000

login admin using following url http://127.0.0.1:8000/admin/

username: admin password: Demo@123