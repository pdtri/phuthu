"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))
#path = '/home/pdtri/myproject'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qr-u4yg5khi*me1gm+18pktb39wetuv&nhmq-^4u*-i*5&iuvo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = os.environ.get('DEBUG')
#TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['phuthu.herokuapp.com']
#'phuthu.herokuapp.com'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.myapp', 
    'apps.chuyenthue',
    'gunicorn',
    'django_tables2',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
"""
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'OPTIONS': {
            'options': '-c search_path=qldd,public'
        },
    }
 }
"""
"""
DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'OPTIONS': {
            'options': '-c search_path=public'
        },
	   'NAME': 'qldd',
       'USER': 'postgres',
       'PASSWORD': 'lumia430',
       'HOST': '127.0.0.1',
       'PORT': '5432',
    }
}
"""
"""

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
	   'OPTIONS': {
            'options': '-c search_path=qldd,public'
        },
	   'NAME': 'd3u8ape305as73',
       'USER': '',
       'PASSWORD': '',
       'HOST': 'ec2-54-225-237-64.compute-1.amazonaws.com',
       'PORT': '5432',
    }
}

"""

DATABASES = {'default': dj_database_url.config()}
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
DATABASES['default']['OPTIONS'] = {
    'options': '-c search_path=qldd,public'
}

#DATABASE_URL = 'postgresql:///qldd'
#DATABASE_URL='heroku pg:psql postgresql-tapered-28118 --app phuthu '
#heroku pg:psql postgresql-tapered-28118 --app phuthu
#DATABASES['default'] = dj_database_url.config(conn_max_age=600)
#DATABASES = {'default': dj_database_url.config()}
#DATABASES['default'] = dj_database_url.config(default='postgres://...')
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
#STATICFILES_DIRS=(
#                  os.path.join(BASE_DIR,'static'),
				  #/Users/ADMIN/OneDrive/hoclamweb/django/qldd/qldd/static/static_root/,
#)
#STATIC_ROOT=os.path.join(BASE_DIR,'live-static','static-root')


STATIC_ROOT = os.path.join(BASE_DIR,'static','static_dirs') # chu y load css

STATICFILES_DIRS=(
                  os.path.join(BASE_DIR,'static','static_root'),
				  #/Users/ADMIN/OneDrive/hoclamweb/django/qldd/qldd/static/static_root/,
)
#STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'),) 

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"live-static","media-root")
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
