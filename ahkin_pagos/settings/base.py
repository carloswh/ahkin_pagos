"""
    Django
"""

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _
from ahkin_pagos.core.settings import Settings

import os
import re
import json
import environ


class BaseSettings(Settings):
    """ Community base settings, don't use this directly. """
    SITE_ROOT = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    env = environ.Env(
        DEBUG=(bool, False),
        SECRET_KEY=str,
    )
    env_path = None
    if os.environ['DJANGO_SETTINGS_MODULE'] == 'ahkin_pagos.settings.dev':
        env_path = os.path.join(SITE_ROOT, '.config_project/environ/dev/.env')

    environ.Env.read_env(env_path)

    SECRET_KEY = env('SECRET_KEY')

    AUTH_USER_MODEL = 'custom_user.User'

    # Debug settings
    DEBUG = env('DEBUG')

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    BEFORE_DJANGO_APPS = [

    ]

    DJANGO_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

    SHARED_PROJECT_APPS = [
        'ahkin_pagos.apps.custom_user',
        'ahkin_pagos.apps.commons',
        'ahkin_pagos.apps.finanzas_admin'
    ]

    THIRD_PARTY_APPS = [
        'debug_toolbar',
    ]

    # Installed apps deben estan todas las apps, tenant, shared, externats y las default de django(admin, auth...)
    INSTALLED_APPS = BEFORE_DJANGO_APPS + SHARED_PROJECT_APPS + DJANGO_APPS + THIRD_PARTY_APPS

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'ahkin_pagos.core.urls.urls_desk'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR+"/templates"],
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

    WSGI_APPLICATION = 'ahkin_pagos.core.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/1.11/ref/settings/#databases

    '''
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'ahkin_pagos',
            'USER': 'ahkin_pagos',
            'PASSWORD': 'ahkin_pagos',
            'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',
            'OPTIONS': {
                #"init_command": "SET storage_engine=InnoDB",
                #"init_command": "SET GLOBAL max_connections = 100000",
            }
        }
    }
    '''
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(SITE_ROOT, '.media')

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

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.11/howto/static-files/

    STATIC_URL = '/static/'