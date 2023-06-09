from pathlib import Path
import os
import dj_database_url
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o#*3wc)1)c!@h9@r0-e46^09y*&y2=la0r==fnse*nf^z6p0ro'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #manual
    'store',
    'whitenoise.runserver_nostatic',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'ecom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'ecom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
       
    #3 New Manual setting for remove postgresql (railway) , put these values below 'NAME' variable in databases and comment out 'ENGINE' and 'NAME'
        'ENGINE': 'django.db.backends.postgresql',
        'URL':'postgresql://postgres:FqqB4CTSpdQqQNJ3AFFU@containers-us-west-8.railway.app:6235/railway',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'FqqB4CTSpdQqQNJ3AFFU',
        'HOST': 'containers-us-west-8.railway.app',
        'PORT': '6235', 
    }
}
"""  #1 default django setting
       'ENGINE': 'django.db.backends.sqlite3',  
       'NAME': BASE_DIR / 'db.sqlite3',


     #2 New Manual setting for local postgresql , put these values below 'NAME' variable in databases and comment out 'ENGINE' and 'NAME'
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': 'ZAQ!zaq1',
        'HOST': 'localhost',
        'PORT': '5432', 
"""


#Manual for vercel deployment
#DATABASES['default'] = dj_database_url.config()


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#manual

#setting up static files


# render images with url, also set the configuration in urls.py
MEDIA_URL = '/images/'

# this will add media in static/images folder as soon as any image is being uploaded
MEDIA_ROOT=os.path.join(BASE_DIR,'static/images')

# vercel
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = 'static/'

STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static"), ]
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"