# coding: utf-8

from unipath import Path
from decouple import config
from dj_database_url import parse as db_url

BASE_DIR = Path(__file__).parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com', '.localhost']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fazenda.core',
    'fazenda.gerenciador', 
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fazenda.urls'

WSGI_APPLICATION = 'fazenda.wsgi.application'


DATABASES = {'default': config('DATABASE_URL', default='sqlite:///' + BASE_DIR.child('db.sqlite3'), cast=db_url)}

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = BASE_DIR.child('staticfiles')
STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR + '/media' # Esta correto ?
MEDIA_URL = '/media/'

STATICFILES_DIRS = ()
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DATE_INPUT_FORMATS = ('%d/%m/%Y')
DECIMAL_SEPARATOR = '.'
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880 # 5MB
