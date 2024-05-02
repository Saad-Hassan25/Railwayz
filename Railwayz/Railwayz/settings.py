"""
Django settings for Railwayz project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import stripe

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)@pn2#_)qrvx!ft=ro#u=oc@ya)ze*jc14ptc3cl%ldj=+qsg3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Bookings',
    'Core',
    'Feedback',
    'Payment',
    'TimeTrackingAndPrediction',
    'UserManagement',
    'Trains',
    'Stations',
    'Schedules',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Railwayz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'Bookings', 'templates'),
            os.path.join(BASE_DIR, 'Core', 'templates'),
            os.path.join(BASE_DIR, 'Feedback', 'templates'),
            os.path.join(BASE_DIR, 'Payment', 'templates'),
            os.path.join(BASE_DIR, 'TimeTrackingAndPrediction', 'templates'),
            os.path.join(BASE_DIR, 'UserManagement', 'templates'),
            os.path.join(BASE_DIR, 'Trains', 'templates'),
            os.path.join(BASE_DIR, 'Schedules', 'templates'),
            os.path.join(BASE_DIR, 'Stations', 'templates'),
            
            ],
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

WSGI_APPLICATION = 'Railwayz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Karachi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    # Add the paths to your app-specific static files here
    os.path.join(BASE_DIR, 'Bookings', 'static'),
    os.path.join(BASE_DIR, 'Core', 'static'),
    os.path.join(BASE_DIR, 'Feedback', 'static'),
    os.path.join(BASE_DIR, 'Payment', 'static'),
    os.path.join(BASE_DIR, 'TimeTrackingAndPrediction', 'static'),
    os.path.join(BASE_DIR, 'UserManagement', 'static'),
    os.path.join(BASE_DIR, 'Trains', 'static'),

]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STRIPE_PUBLISHABLE_KEY = 'pk_test_51OLi3ALYWee0pOU1kWHMuhXAoNhW5gAARHBgBVO6x9H5aYWwPC7WFQrlF3pC61SPYVL1AYVQyI1Kq0K01a7blhT200sL6U4pXX'
STRIPE_SECRET_KEY = 'sk_test_51OLi3ALYWee0pOU1I27z39rheeMmzKMzIxcBrvJydYY6NBU32OCE6x7EvuwKJMhYeBkidCWUSNqiMPSWn0Kp8njP00AWn3np7h'
