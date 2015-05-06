"""
Django settings for pybursa project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+3xkamw7ly*-n#lb@+28@)c*4&r+$hl6#&c0e7@7p7e)a)7(bq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'quadratic',
    'courses',
    'students',
    'coaches',
    'feedbacks'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pybursa.urls'

WSGI_APPLICATION = 'pybursa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

EMAIL_HOST = 'localhost'
EMAIL_PORT =  1025

ADMINS = (('Oleg', 'khazar65@mail.ru'), )

LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        
        'loggers': {
            'courses': {
                'level': 'DEBUG',
                'handlers': ['null', 'console_courses', 'file_courses'],
                'propagate': True,
            },
            'students': {
                'level': 'WARNING',
                'handlers': ['console_students', 'file_students'],
                'propagate': True,
            }
        },
        
        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'logging.NullHandler',
            },
            'console_courses': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'console_students': {
                'level': 'WARNING',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
        
            'file_courses': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, 'courses/debug.log'),
                'formatter': 'simple'
            },
            'file_students': {
                'level': 'WARNING',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, 'students/debug.log'),
                'formatter': 'verbose'
            }
        },

        'formatters': {
            'verbose': {
                'format': '%(asctime)s %(levelname)s %(module)s in %(funcName)s - %(message)s'
            },
            'simple': {
                'format': '%(levelname)s - %(message)s'
            }
        }
}