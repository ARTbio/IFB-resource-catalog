# IFB-resource-catalog
Catalog of bioinformatics resources of the French Institute of Bioinformatics (IFB)

## How to install the IFB-resource-catalog:
  $ git clone https://github.com/IFB-ElixirFr/IFB-resource-catalog.git
### Install prerequisite:
  $ sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
### Setup a virtualenv 
  $ sudo pip3 install virtualenv 
  
  $ virtualenv venv
  
  $ source venv/bin/activate
### Install Django prerequisite:
  $ pip install django-filter
  
  $ pip install django-rest-framework
  
  $ pip install django-widget-tweaks
  
  $ pip install psycopg2
  
  $ pip install requests
  
  $ pip install django_extensions
  
### Setup a database:
  $ sudo service postgresql start
  
  $ sudo -i -u postgres
  
  $ psql
  
  $ CREATE USER user_name;
  
  $ CREATE DATABASE database_name OWNER user_name;
  
  $ ALTER USER user_name WITH PASSWORD ‘password_here’;
  
### Configure the database in settings.py file
### Run a Django migration
  $ python manage.py migrate
  
  $ python manage.py makemigrations
### Start the server
  $ python manage.py runserver
