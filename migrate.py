#!/usr/bin/env python

import environ
from django.conf import settings
from django.http import HttpResponse
from django.urls import path


env = environ.Env()
DB_USER = env('POSTGRES_USER', default='')
DB_PASSWORD = env('POSTGRES_PASSWORD', default='')
DB_PORT = env('POSTGRES_PORT', default='')
DB_NAME = env('POSTGRES_DB', default='')
DB_HOST = env('POSTGRES_HOST', default='')
DB_CONFIG_URL = f'postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
DB_DEFAULT = env.db('DATABASE_URL', default=DB_CONFIG_URL)
DB_DEFAULT["ATOMIC_REQUESTS"] = True


settings.configure(
    # development
    DEBUG=True,
    # base
    ALLOWED_HOSTS=['*'],
    ROOT_URLCONF=__name__,
    # db
    DB_USER=DB_USER,
    DB_PASSWORD=DB_PASSWORD,
    DB_PORT=DB_PORT,
    DB_NAME=DB_NAME,
    DB_HOST=DB_HOST,
    DB_CONFIG_URL=DB_CONFIG_URL,
    DATABASES={'default': DB_DEFAULT},
)


urlpatterns = [
    path('', lambda request: HttpResponse('Hello World!')),
]


def handler(event, context):
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'migrate'])
