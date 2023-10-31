import mimetypes
import os

from .environments import BASE_DIR

APPEND_SLASH = False

ALLOWED_HOSTS = ["*"]
DATA_UPLOAD_MAX_MEMORY_SIZE = 100214400
FILE_UPLOAD_MAX_MEMORY_SIZE = 100214400
DATA_UPLOAD_MAX_NUMBER_FIELDS = 100214400

INSTALLED_APPS = [
    # apps
    "users",
    "tenants",
    # libs
    'django_filters',
    "jazzmin",
    "drf_yasg",
    "rest_framework",
    "corsheaders",
    # default
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django_tenants.middleware.TenantSubfolderMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "core.middlewares.DisableCSRF",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "core.middlewares.APIAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
TENANT_MODEL = "tenants.Client"

TENANT_DOMAIN_MODEL = "tenants.Domain"
ROOT_URLCONF = "core.urls"
TENANT_SUBFOLDER_PREFIX = "bazar"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                'django.template.context_processors.request',
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "users.UserBase"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kathmandu"

LANGUAGE_CODE = "en-us"

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

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

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

mimetypes.add_type("application/javascript", ".js", True)
mimetypes.add_type("text/css", ".css", True)

WHITENOISE_MIMETYPES = {".js": "application/javascript", ".css": "text/css"}

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

CKEDITOR_UPLOAD_PATH = "media/ckeditor_uploads/"
