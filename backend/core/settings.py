import os
from datetime import timedelta
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured


# =========================================================
# BASE
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

for _dotenv in (BASE_DIR / ".env", BASE_DIR.parent / ".env"):
    if _dotenv.is_file():
        load_dotenv(_dotenv)
        break


# =========================================================
# BASIC SETTINGS
# =========================================================

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "DjangoProdFallbackKey-2026-ChangeThisImmediately-9xK7mP2qL8",
)

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = [
    "pizzas.pythonanywhere.com",
    "localhost",
    "127.0.0.1",
]

# =========================================================
# APPLICATIONS
# =========================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party
    "whitenoise.runserver_nostatic",
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "corsheaders",
    "django_filters",
    "channels",
    "django_celery_beat",

    # Local apps
    "accounts",
    "inventory",
    "orders",
    "payments",
    "notifications",
    "dashboard",
]


# =========================================================
# MIDDLEWARE
# =========================================================

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
]


# =========================================================
# URL / WSGI / ASGI
# =========================================================

ROOT_URLCONF = "core.urls"

WSGI_APPLICATION = "core.wsgi.application"

ASGI_APPLICATION = "core.asgi.application"


# =========================================================
# TEMPLATES
# =========================================================

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


# =========================================================
# DATABASE - AIVEN MYSQL
# =========================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# =========================================================
# USER MODEL
# =========================================================

AUTH_USER_MODEL = "accounts.User"


# =========================================================
# PASSWORD VALIDATION
# =========================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        )
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        )
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        )
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        )
    },
]


# =========================================================
# INTERNATIONALIZATION
# =========================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# =========================================================
# STATIC / MEDIA
# =========================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# =========================================================
# DEFAULT PRIMARY KEY
# =========================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# =========================================================
# DJANGO REST FRAMEWORK
# =========================================================

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),

    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),

    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ),

    "DEFAULT_PAGINATION_CLASS": (
        "rest_framework.pagination.PageNumberPagination"
    ),

    "PAGE_SIZE": 12,

    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.ScopedRateThrottle",
    ],

    "DEFAULT_THROTTLE_RATES": {
        "auth": "10/min",
        "contact": "5/hour",
    },
}


# =========================================================
# JWT
# =========================================================

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),

    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),

    "ROTATE_REFRESH_TOKENS": True,

    "BLACKLIST_AFTER_ROTATION": True,

    "AUTH_HEADER_TYPES": ("Bearer",),

    "AUTH_TOKEN_CLASSES": (
        "rest_framework_simplejwt.tokens.AccessToken",
    ),

    "TOKEN_TYPE_CLAIM": "token_type",
}


# =========================================================
# CORS
# =========================================================

CORS_ORIGINS = os.getenv(
    "CORS_ORIGINS",
    "http://localhost:5173,"
    "http://127.0.0.1:5173,"
    "http://localhost:5174,"
    "http://127.0.0.1:5174",
)

CORS_ALLOWED_ORIGINS = [
    origin.strip().rstrip("/")
    for origin in CORS_ORIGINS.split(",")
    if origin.strip()
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_ALL_ORIGINS = False

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

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]


# =========================================================
# CSRF
# =========================================================

CSRF_TRUSTED_ORIGINS = [
    "https://pizzas.pythonanywhere.com",
]


# =========================================================
# FRONTEND URL
# =========================================================

FRONTEND_URL = os.getenv(
    "FRONTEND_URL",
    "http://localhost:5173",
).rstrip("/")


# =========================================================
# EMAIL
# =========================================================

EMAIL_BACKEND = os.getenv(
    "EMAIL_BACKEND",
    (
        "django.core.mail.backends.console.EmailBackend"
        if DEBUG
        else "django.core.mail.backends.smtp.EmailBackend"
    ),
)

EMAIL_HOST = os.getenv(
    "EMAIL_HOST",
    "smtp.gmail.com",
)

EMAIL_PORT = int(
    os.getenv("EMAIL_PORT", "587")
)

EMAIL_USE_TLS = (
    os.getenv("EMAIL_USE_TLS", "True").lower() == "true"
)


EMAIL_HOST_USER = os.getenv(
    "EMAIL_HOST_USER",
    "connectwithashurana@gmail.com",
)

EMAIL_HOST_PASSWORD = os.getenv(
    "EMAIL_HOST_PASSWORD",
    "dhsm ensv ubwi juxd",
)

DEFAULT_FROM_EMAIL = os.getenv(
    "DEFAULT_FROM_EMAIL",
    "connectwithashurana@gmail.com",
)

ADMIN_EMAIL = os.getenv(
    "ADMIN_EMAIL",
    "connectwithashurana@gmail.com",
)

# =========================================================
# RAZORPAY
# =========================================================

RAZORPAY_KEY_ID = os.getenv(
    "RAZORPAY_KEY_ID",
    "",
)

RAZORPAY_KEY_SECRET = os.getenv(
    "RAZORPAY_KEY_SECRET",
    "",
)


# =========================================================
# REDIS / CHANNELS / CELERY
# =========================================================
# REDIS_URL is optional. Local/managed deploys set it to enable Celery and
# live (channel-layer) order updates. When it is absent (e.g. a free
# PythonAnywhere account has no Redis) Celery runs tasks eagerly and the
# channel layer is in-memory, so nothing crashes for lack of a broker.

REDIS_URL = os.getenv("REDIS_URL")

if REDIS_URL:
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [REDIS_URL],
            },
        },
    }
else:
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels.layers.InMemoryChannelLayer",
        },
    }

CELERY_BROKER_URL = REDIS_URL or "memory://"

CELERY_RESULT_BACKEND = REDIS_URL or "memory://"

if not REDIS_URL:
    CELERY_TASK_ALWAYS_EAGER = True

CELERY_BEAT_SCHEDULER = (
    "django_celery_beat.schedulers:DatabaseScheduler"
)

CELERY_ACCEPT_CONTENT = ["json"]

CELERY_TASK_SERIALIZER = "json"


# =========================================================
# INVENTORY
# =========================================================

LOW_STOCK_THRESHOLDS = {
    "base": 20,
    "sauce": 15,
    "cheese": 15,
    "vegetable": 10,
}


# =========================================================
# ORDER / BILLING
# =========================================================

GST_PERCENT = float(
    os.getenv("GST_PERCENT", "5")
)

DELIVERY_CHARGE = float(
    os.getenv("DELIVERY_CHARGE", "40")
)


# =========================================================
# TOKEN EXPIRATION
# =========================================================

EMAIL_VERIFICATION_TOKEN_EXPIRY_HOURS = int(
    os.getenv(
        "EMAIL_VERIFICATION_TOKEN_EXPIRY_HOURS",
        "24",
    )
)

PASSWORD_RESET_TOKEN_EXPIRY_MINUTES = int(
    os.getenv(
        "PASSWORD_RESET_TOKEN_EXPIRY_MINUTES",
        "30",
    )
)


# =========================================================
# PRODUCTION SECURITY / HTTPS
# =========================================================

if not DEBUG:

    # Render HTTPS proxy
    SECURE_PROXY_SSL_HEADER = (
        "HTTP_X_FORWARDED_PROTO",
        "https",
    )

    # Redirect HTTP -> HTTPS
    SECURE_SSL_REDIRECT = True

    # Secure cookies
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # HSTS
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    # Security headers
    SECURE_CONTENT_TYPE_NOSNIFF = True

    X_FRAME_OPTIONS = "DENY"

    SECURE_REFERRER_POLICY = "same-origin"