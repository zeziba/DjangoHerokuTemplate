"""
Django settings for django_heroku_template project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import logging
from pathlib import Path
import environ
import os
import dj_database_url
import django_heroku

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_FOLDER_DIR = env("DEFAULT_PROJECT_FOLDER_NAME")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)  # type: ignore

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default="[*]")  # type: ignore


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.users",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = f"{ PROJECT_FOLDER_DIR }.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "apps", "templates"),
        ],
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


TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.request",
]

WSGI_APPLICATION = f"{ PROJECT_FOLDER_DIR }.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASE_TYPE = os.environ.get("DATABASE_TYPE", "sqlite")
DATABASE_PATH = os.environ.get("SQL_HOST", f"db.{DATABASE_TYPE}")
if not os.path.isdir("databases"):
    os.mkdir("databases")
DATABASE_PATH = f"{DATABASE_TYPE}:///{ os.path.join('databases', DATABASE_PATH)}.{env('DATABASE_FILE_EXTENSION')}"
DATABASES = {"default": env.db(default=DATABASE_PATH)}  # type: ignore

# Change 'default' database configuration with $DATABASE_URL.
database_env_update = dj_database_url.config(
    default=DATABASE_PATH, conn_max_age=500, ssl_require=True
)
DATABASES["default"].update(database_env_update)

# Fix an error that occurs in development enviroment due to using sqlite3 instead of a differnt database engine
del DATABASES["default"]["OPTIONS"]["sslmode"]  # type: ignore


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# Auth
AUTH_USER_MODEL = "users.Account"

# Caching
# https://docs.djangoproject.com/en/3.0/topics/cache/
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "cache",
    }
}

# Email backend
EMAIL_BACKEND = env("EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")  # type: ignore
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = 587
EMAIL_USE_TLS = env.bool("", default=True)  # type: ignore
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_DEST = env("EMAIL_DEST")

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = []

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "sass_processor.finders.CssFinder",
    "compressor.finders.CompressorFinder",
]

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(STATIC_ROOT, "mediafiles")

# Simplified static file serving.
STATICFILES_STORAGE = env("STATIC_FILE_STORAGE")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Log everything to the console, including tracebacks
LOGGING = {
    "version": 1,
    "disable_existing_loggers": env.bool("DISABLE_EXISTING_LOGGERS", default=False),  # type: ignore
    "root": {"handlers": ["console"], "level": "DEBUG"},
    "handlers": {
        "console": {
            "level": env("DJANGO_LOG_LEVEL"),
            "class": "logging.StreamHandler",
            "formatter": "simple",
        }
    },
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
}

# Suppress "Starting new HTTPS connection" messages
logging.getLogger("requests.packages.urllib3.connectionpool").setLevel(logging.ERROR)

# SSL
ENABLE_SSL = env.bool("ENABLE_SSL", default=True)  # type: ignore
SESSION_COOKIE_SECURE = ENABLE_SSL
CSRF_COOKIE_SECURE = ENABLE_SSL
# SECURE_SSL_REDIRECT = ENABLE_SSL
if ENABLE_SSL:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Django Sass
SASS_PROCESSOR_ROOT = STATIC_ROOT
SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(SASS_PROCESSOR_ROOT, "scss"),
    os.path.join(SASS_PROCESSOR_ROOT, "vendor", "node_modules"),
]

# SASS bugfix
SASS_PRECISION = 8
SASS_OUTPUT_STYLE = "compact"

# Compress
COMPRESS_ROOT = os.path.join(STATIC_ROOT, "compress")

# Node model URL
NODE_MODULES_URL = os.path.join(STATIC_URL, "node_modules/")

# Activate Django-Heroku.
django_heroku.settings(locals())
