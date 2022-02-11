"""
Django settings for puresizer-landing project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from time import strftime

from sizer.db_conf import DB_NAME, DB_PASSWORD, DB_USER

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APPEND_SLASH = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "qvu@7-0*@+kxeknyi$a)&)=ujh(7m5a!&@*#e_38$o#^(j@$7d"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Comment the below line to ENABLE login auth
# os.environ["DEV_SIZER"] = "yes"

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "env_setup",
    "rest_framework",
    "corsheaders",
]
LOGIN_EXEMPT_URLS = [r"^scenario/salesforce/$"]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "sizer.middleware.exception.ExceptionMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

DEV_ENVIRONMENT = os.environ.get("DEV_SIZER", "no")

APP_LIST = ['fa-sizer', 'fb-sizer', 'fr-sizer']

APP_URLS = {
    'fa-sizer': 'https://dev-fa-sizer.salestools.purestorage.com/fa-sizer',
    'fb-sizer': 'https://dev-fa-sizer.salestools.purestorage.com/fb-sizer',
    'fr-sizer': 'https://dev-fa-sizer.salestools.purestorage.com/fr-sizer'
}

if DEV_ENVIRONMENT == "yes":
    CORS_ORIGIN_ALLOW_ALL = True
    DEV_SIZER = True

    CLIENT_ID = "0oa6mvqci6eYzIJq8357"
    REDIRECT_URL = "http%3A%2F%2F127.0.0.1%3A8001%2Flogin%2Fokta"
    APP_URL = "https://dev-601430.okta.com/oauth2/default/v1"

    LOGIN_REDIRECT_ADDR = "http://127.0.0.1:8000/landing-app/index.html"

    LOGOUT_REDIRECT_ADDR = "http://127.0.0.1:8000/landing/login"

    SERVER_ADDRESS = "127.0.0.1"
    PORT = "8000"

else:
    DEV_SIZER = False
    CLIENT_ID = "0oa1i20ucvrIJrham1d8"
    REDIRECT_URL = "https%3A%2F%2Fdev%2Dfa%2Dsizer%2Esalestools%2Epurestorage%2Ecom%2Flanding%2Flogin%2Fokta"
    APP_URL = "https://purestorage.okta.com/oauth2/v1"
    LOGOUT_REDIRECT_ADDR = "https://dev-fa-sizer.salestools.purestorage.com/landing/#/login"
    SERVER_ADDRESS = "dev-fa-sizer.salestools.purestorage.com"
    PORT = "443"

    AUTHZERO_CLIENT_ID = 'Dca9g7W8P8kNoyIeSDDZumAD7lhOjvIJ'
    AUTHZERO_CLIENT_SECRET = 'kKnuRo-p-KgBadpgHd1Kn2fSL_dNzX8NTfg_nnLbdRXX-ShuUdQ83RMMthEubOdS'
    AUTHZERO_REDIRECT_URI = 'https%3A%2F%2Fdev-fa-sizer.salestools.purestorage.com%2Flanding%2Flogin%2Fauthzero'
    AUTHZERO_AUTHORIZE_URL = 'https://authportal-web-external.staging-cloud-support.purestorage.com/sso/oauth2/authorize'
    AUTHZERO_TOKEN_URL = 'https://authportal-web-external.staging-cloud-support.purestorage.com/oauth/token'
    AUTHZERO_USERINFO_URL = 'https://staging-purestorage.auth0.com/userinfo'

if DEV_SIZER:
    ROOT_URLCONF = "sizer.dev_header_url"
else:
    ROOT_URLCONF = "sizer.urls"

# ROOT_URLCONF = "sizer.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "sizer.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

UI_ROOT = os.path.join(BASE_DIR, "sizer/webapps/dist/landing-static/")
UI_URL = "ui/"
STATICFILES_DIRS = (UI_ROOT,)

MEDIA_ROOT = os.path.join(BASE_DIR, "report/")

STATIC_URL = "/landing-static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "add_detail": {"()": "sizer.log_filter.AddOppSiteDetail"},
        "sizing_debug_true": {"()": "sizer.log_filter.ProductionSizingLog"},
    },
    "formatters": {
        "error": {
            "format": "[%(asctime)s][line:%(lineno)s] - %(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
        "detailed": {
            "format": "[%(asctime)s][%(levelname)s][file:%(filename)s: %(lineno)s] - %(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
    },
    "handlers": {
        "default": {
            "level": "WARNING",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(
                BASE_DIR, f"logs/server_logs/{strftime('%d-%m-%Y')}.log"
            ),
            # 5MB file size
            "maxBytes": 5000000,
            "backupCount": 5,
            "formatter": "error",
        },
        "app_handler": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(
                BASE_DIR, f"logs/server_logs/{strftime('%d-%m-%Y')}.log"
            ),
            # 5MB file size
            "maxBytes": 5000000,
            "backupCount": 5,
            "formatter": "detailed",
            "filters": ["add_detail", "sizing_debug_true"],
        },
    },
    "loggers": {
        "": {"level": "WARNING", "handlers": ["default"]},
        "core": {"level": "INFO", "handlers": ["app_handler"]},
        "env_setup": {"level": "INFO", "handlers": ["app_handler"]},
    },
}
