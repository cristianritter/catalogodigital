import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

IS_HEROKU_APP = "DYNO" in os.environ and not "CI" in os.environ

CSRF_TRUSTED_ORIGINS = ['https://admin.mk4digital.com']

#IMPORT_EXPORT_USE_TRANSACTIONS = True
if not IS_HEROKU_APP:
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    SUBDOMAIN_DOMAIN = "localhost"

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': BASE_DIR /'tmp/django_cache',
        }
    }
else:
    DEBUG = False
    ALLOWED_HOSTS = ['.mk4digital.com', '*.mk4digital.com']
    SUBDOMAIN_DOMAIN = "mk4digital.com"
    CACHES = {
        'default': {
            # Use django-bmemcached
            'BACKEND': 'django_bmemcached.memcached.BMemcached',
            'TIMEOUT': None,
            'LOCATION': os.environ['MEMCACHIER_SERVERS'],
            'OPTIONS': {
                'username': os.environ['MEMCACHIER_USERNAME'],
                'password': os.environ['MEMCACHIER_PASSWORD'],
            }
        }
    }

ROOT_URLCONF = "catalogodigital.urls"
SUBDOMAIN_URLCONFS = {
    None: 'landingpages.urls', 
    'www': 'landingpages.urls',
    'landingpage': 'landingpages.urls',
    'loja': 'lojas.urls',
    'admin': 'admin.urls',
}


COMPRESS_ENABLED =  DEBUG

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.admin",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'import_export',
    'compressor',
    'landingpages',
    'lojas',
]

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware", 
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "subdomains.middleware.SubdomainURLRoutingMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if IS_HEROKU_APP:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('SUPABASE_DB_NAME'),
            'USER': os.getenv('SUPABASE_USER'),
            'PASSWORD': os.getenv('SUPABASE_PASSWORD'),
            'HOST': os.getenv('SUPABASE_HOST'), # ou o endereço do seu banco de dados
            'PORT': os.getenv('SUPABASE_PORT'), # ou a porta do seu banco de dados
            #'OPTIONS': {
            #    'sslmode': 'verify-full',
            #    'sslrootcert': 'catalogodigital/prod-ca-2021.crt', #precisa hospedar em algum lugar
            #}
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

COMPRESS_OFFLINE = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "catalogodigital.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
COMPRESS_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

