from datetime import timedelta
from email.policy import default
import os
from pathlib import Path

# from telnetlib import AUTHENTICATION

from environs import Env
from decouple import config

env = Env()
env.read_env()


BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = env.str(
#     "SECRET_KEY",
#     default="django-insecure-0m*%6s^7)i$yz@#fiu$nx+7qfs(p8m%72j8_m$v&24cryi8%e#",
# )

SECRET_KEY = config("SECRET_KEY")

# DEBUG = env.bool("DEBUG", default=True)
DEBUG = True

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])


INSTALLED_APPS = [
    "chat",
    "channels",
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "djoser",
    "accounts",
    "social_django",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",  # make more smoothly when making migrations
]
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

CORS_ALLOW_ALL_ORIGINS = True

MIDDLEWARE = [
    # "django.middleware.csrf.CsrfViewMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "auth_system.urls"

# AUTH_USER_MODEL = "accounts.User"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "build")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

# WSGI_APPLICATION = "auth_system.wsgi.application"
ASGI_APPLICATION = "auth_system.asgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": env.str("DB_NAME", default="diplomka"),
#         "USER": env.str("DB_USER", default="postgres"),
#         "PASSWORD": env.str("DB_PASSWORD", default="A78J79Zh01"),
#         "HOST": env.str("DB_HOST", default="localhost"),
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "HOST": config("DB_HOST"),
        "PASSWORD": config("DB_PASSWORD"),
        "PORT": config("DB_PORT"),
    }
}


# AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
# AWS_S3_SIGNATURE_VERSION = config("AWS_S3_SIGNATURE_VERSION")
# AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME")
# AWS_S3_FILE_OVERWRITE = config("AWS_S3_FILE_OVERWRITE")
# AWS_DEFAULT_ACL = config("AWS_DEFAULT_ACL")
# AWS_S3_VERITY = config("AWS_S3_VERITY")
# DEFAULT_FILE_STORAGE = config("DEFAULT_FILE_STORAGE")

AWS_ACCESS_KEY_ID = "AKIA47GCABNKRMS223DJ"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "zhzh"
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_S3_REGION_NAME = "eu-north-1"
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"


# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [("127.0.0.1", 6379)],
#         },
#     },
# }


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [
                f"rediss://:{config('REDIS_PASSWORD')}@{config('REDIS_URL')}:{config('REDIS_PORT')}"
            ],
        },
    },
}


# EMAIL_BACKEND = env.str(
#     "EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
# )

EMAIL_BACKEND = config("EMAIL_BACKEND")

# EMAIL_BACKEND = env.str(
#     "EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
# )


# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default="bkrvj83@gmail.com")
# EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default="mamj uppa hdbd bger")
# EMAIL_USE_TLS = True

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True


# yreauqtumfktptyv
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


STATICFILES_DIRS = [os.path.join(BASE_DIR, "build/static")]

STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_ROOT = "media/"
# MEDIA_URL = "/media/"
MEDIA_URL = "https://{zhzh}.s3.eu-north-1.amazonaws.com/media/"


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

# D:\auth_system\myenv\Lib\site-packages\rest_framework_simplejwt\authentication.py

AUTHENTICATION_BACKENDS = {
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",  # in order to make email and password login that we implement it still continue to work
}

# added simple jwt

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=365),
    "USER_ID_FIELD": "email",
    "TOKEN_SERIALIZER": "accounts.serializers.CustomTokenObtainPairSerializer",
    "JWT_PAYLOAD_HANDLER": "accounts.apps.my_jwt_payload_handler",
}

DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "SET_USERNAME_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SERIALIZERS": {
        "user": "accounts.serializers.UserSerializer",
        "user_delete": "djoser.serializers.UserDeleteSerializer",
    },
}


AUTH_USER_MODEL = "accounts.UserAccount"
