# Django Rindus_Bank

This is a simple CRUD app built in Django and python3 for manage personal accounts.

## Project Requisites

'''
-Administrators of the app should authenticate using a Google account
-Administrators should be able to create, read, update and delete users
-Restrict manipulation operations on a user to the administrator who created them
-Use PostgreSQL as the database backend
-Use Python 3.x
'''
## Plugin and libraries
'''
psycopg2  ->  connect Django with Postgres
social-auth-app-django  -> social auth for google accounts
django-localflavor  -> check IBAN fields
'''

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need a system with docker-compose.

### Installing
'''
1- Clone this repo -> git clone https://github.com/jkdc/django_rindus_bank.git
2- Go to folder cloned -> cd django_rindus_bank
3- Run docker-compose -> docker-compose up
4- Open a terminal and execute:
4.1- docker-compose exec web python manage.py makemigrations
4.2- docker-compose exec web python manage.py migrate
5- Go to localhost:8000
'''

## Authors

* **Joaquín Carodoso**

