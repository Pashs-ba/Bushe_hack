"""Django settings for backend project."""

import datetime
from pathlib import Path

import toml

SETTINGS_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = Path(SETTINGS_DIR).parent


config = toml.load(BASE_DIR / "config.toml")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SECRET_KEY = config["Django"]["SECRET_KEY"]

DEBUG = config["Django"]["DEBUG"]
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Apps
    "backend.apps.authentication.apps.AuthConfig",
    "backend.apps.blog.apps.BlogConfig",
    "backend.apps.core.apps.CoreConfig",
    "backend.apps.notifications.apps.NotificationsConfig",
    "backend.apps.timetable.apps.TimetableConfig",
    "backend.apps.homework.apps.HomeworkConfig",
    "backend.apps.minimum.apps.MinimumConfig",
    # Third-party apps
    # "whitenoise.runserver_nostatic",
    "corsheaders",
    "rest_framework",
    "django_filters",
    "rest_framework_simplejwt.token_blacklist",
    "sorl_thumbnail_serializer",
    "sorl.thumbnail",
    # Auth
    "djoser",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

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

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# TODO: Change to PostgreSQL.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = "ru"
TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "dist" / "static"
STATICFILES_DIRS = []
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = "media"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "authentication.User"

DATE_INPUT_FORMATS = ["%Y-%m-%d", "%d-%m-%Y"]


REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 50,
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DATE_INPUT_FORMATS": ["%d-%m-%Y"],
}

JWT_AUTH = {
    "TOKEN_TYPE_CLAIM": "rest_framework_simplejwt.tokens.AccessToken",
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=14),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": True,
    "AUTH_HEADER_TYPES": ("JWT",),
}


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


# Email
DEFAULT_FROM_EMAIL = config["Email"]["DEFAULT_FROM_EMAIL"]
EMAIL_HOST = config["Email"]["EMAIL_HOST"]
EMAIL_PORT = config["Email"]["EMAIL_PORT"]
EMAIL_HOST_USER = config["Email"]["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = config["Email"]["EMAIL_HOST_PASSWORD"]
EMAIL_USE_TLS = config["Email"]["EMAIL_USE_TLS"]


# Users
DJOSER = {
    "SEND_ACTIVATION_EMAIL": True,
    "ACTIVATION_URL": "api/auth/activate/{uid}/{token}",
    "EMAIL": {
        "activation": "backend.apps.authentication.email.ActivationEmail",
    },
}

PROTOCOL = "http"
DOMAIN = "localhost:8000"


# ------------ DiaryX ------------

DIARYX_SCHOOL_NAME = config["Diaryx"]["SCHOOL_NAME"]
DIARYX_SCHOOL_FULL_NAME = config["Diaryx"]["SCHOOL_FULL_NAME"]
DIARYX_PLUGINS = config["Diaryx"]["PLUGINS"]
DIARYX_SCHOOL_N = config["Diaryx"]["SCHOOL_N"]
