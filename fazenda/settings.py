import dj_database_url
from unipath import Path
BASE_DIR = Path(__file__).parent

SECRET_KEY = '1o$+gx5uw@rgtwypmkro&hqqujra_g01ju@xs9ojucytidz)o5'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fazenda.core', 
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


DATABASES = {'default': dj_database_url.config(default='sqlite:///' + BASE_DIR.child('db.sqlite3'))}

LANGUAGE_CODE = 'en-us'

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