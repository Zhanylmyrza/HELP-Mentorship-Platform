from datetime import timedelta
from email.policy import default
import os
from pathlib import Path

from environs import Env
from decouple import config

env = Env()
env.read_env()


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config("SECRET_KEY")

# DEBUG = env.bool("DEBUG", default=True)
DEBUG = True
import certifi

os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
os.environ["SSL_CERT_FILE"] = certifi.where()

# Добавьте эти настройки S3
AWS_S3_USE_SSL = True
AWS_S3_VERIFY = certifi.where()


import urllib3

urllib3.disable_warnings()
AWS_S3_VERIFY = False

# ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

# ALLOWED_HOSTS = [
#     os.environ.get("EC2_IP", "13.61.11.193"),
#     "localhost",
#     "127.0.0.1",
#     "*",
# ]

# rfrbv nj xelysv j,hfpjv yt cj[hfyztncmcz njtcnm rjhjxt]


INSTALLED_APPS = [
    "storages",
    "chat",
    "channels",
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "whitenoise.runserver_nostatic",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "djoser",
    "auth_system",
    "accounts",
    "social_django",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
]


ROOT_URLCONF = "auth_system.urls"


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

ASGI_APPLICATION = "auth_system.asgi.application"


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


AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
AWS_S3_SIGNATURE_VERSION = config("AWS_S3_SIGNATURE_VERSION")
AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME")
AWS_S3_FILE_OVERWRITE = config("AWS_S3_FILE_OVERWRITE")
AWS_DEFAULT_ACL = "public-read"
AWS_DEFAULT_ACL = config("AWS_DEFAULT_ACL")
AWS_S3_VERIFY = config("AWS_S3_VERIFY")
# DEFAULT_FILE_STORAGE = config("DEFAULT_FILE_STORAGE")

AWS_S3_CUSTOM_DOMAIN = (
    f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
)

AWS_S3_USE_SSL = True


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "build/static")]
# STATIC_URL = "static/"
# STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"


MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"
MEDIA_ROOT = ""

# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
#     },
#     "staticfiles": {
#         "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
#     },
# }
# STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}

AWS_LOCATION = "static"


AWS_QUERYSTRING_AUTH = False


# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [
#                 f"rediss://:{config('REDIS_PASSWORD')}@{config('REDIS_URL')}:{config('REDIS_PORT')}"
#             ],
#         },
#     },
# }


EMAIL_BACKEND = config("EMAIL_BACKEND")
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True


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


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Update ALLOWED_HOSTS to properly handle your domain
ALLOWED_HOSTS = [
    "13.61.11.193",
    "localhost",
    "127.0.0.1",
]

# Update CORS settings to allow WebSocket connections
CORS_ALLOWED_ORIGINS = [
    "http://13.61.11.193",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
]

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http://\d+\.\d+\.\d+\.\d+$",
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [
                f"rediss://:{config('REDIS_PASSWORD')}@{config('REDIS_URL')}:{config('REDIS_PORT')}"
            ],
            "ssl_cert_reqs": None,  # Add this for SSL verification in production
            "retry_on_timeout": True,  # Add retry mechanism
            "socket_connect_timeout": 30,  # Increase timeout
        },
    },
}


SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True


# MEDIA_ROOT = "media/"
# # MEDIA_URL = "/media/"
# MEDIA_URL = "https://{zhzh}.s3.eu-north-1.amazonaws.com/"


# REST_FRAMEWORK = {
#     "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
#     "DEFAULT_AUTHENTICATION_CLASSES": [
#         "rest_framework_simplejwt.authentication.JWTAuthentication",
#     ],
# }


# AUTHENTICATION_BACKENDS = {
#     "social_core.backends.google.GoogleOAuth2",
#     "django.contrib.auth.backends.ModelBackend",
# }


# SIMPLE_JWT = {
#     "AUTH_HEADER_TYPES": ("JWT",),
#     "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=365),
#     "USER_ID_FIELD": "email",
#     "TOKEN_SERIALIZER": "accounts.serializers.CustomTokenObtainPairSerializer",
#     "JWT_PAYLOAD_HANDLER": "accounts.apps.my_jwt_payload_handler",
# }

# DJOSER = {
#     "LOGIN_FIELD": "email",
#     "USER_CREATE_PASSWORD_RETYPE": True,
#     "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
#     "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
#     "SEND_CONFIRMATION_EMAIL": True,
#     "SET_USERNAME_RETYPE": True,
#     "SET_PASSWORD_RETYPE": True,
#     "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
#     "USERNAME_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
#     "ACTIVATION_URL": "activate/{uid}/{token}",
#     "SEND_ACTIVATION_EMAIL": True,
#     "SERIALIZERS": {
#         "user": "accounts.serializers.UserSerializer",
#         "user_delete": "djoser.serializers.UserDeleteSerializer",
#     },
# }


# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
# ]

CORS_ALLOW_ALL_ORIGINS = True

# MIDDLEWARE = [
#     "social_django.middleware.SocialAuthExceptionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "whitenoise.middleware.WhiteNoiseMiddleware",
#     "corsheaders.middleware.CorsMiddleware",
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]

# Authentication settings

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
}

AUTHENTICATION_BACKENDS = (
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=365),
    "USER_ID_FIELD": "email",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
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
        "user_create": "accounts.serializers.UserCreateSerializer",
        "user": "accounts.serializers.UserSerializer",
        "current_user": "accounts.serializers.UserSerializer",
        "user_delete": "djoser.serializers.UserDeleteSerializer",
    },
}

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "http://127.0.0.1:8001",
#     "http://13.61.11.193",
# ]

CORS_ALLOW_CREDENTIALS = True

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

AUTH_USER_MODEL = "accounts.UserAccount"
