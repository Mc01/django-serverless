import os

import environ


# env
env = environ.Env()

# development
DEBUG = True

# base
SECRET_KEY = env('SECRET_KEY', default='')
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# static
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# db
DB_USER = env('POSTGRES_USER', default='')
DB_PASSWORD = env('POSTGRES_PASSWORD', default='')
DB_PORT = env('POSTGRES_PORT', default='')
DB_NAME = env('POSTGRES_DB', default='')
DB_HOST = env('POSTGRES_HOST', default='')
DB_CONFIG_URL = f'postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
DB_DEFAULT = env.db('DATABASE_URL', default=DB_CONFIG_URL)
DB_DEFAULT["ATOMIC_REQUESTS"] = True
DATABASES = {'default': DB_DEFAULT}

# apps
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

# rest framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}
