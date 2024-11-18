"""
Django settings for patientordersystem project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-eubv%df3ic(@!9)_ctsg^9svwtj*%=c_cfi^qvzs@7awn^vcv4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# settings.py

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_SECURE = True
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',

    'orders',
    'users',
]

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
# }
# AUTH_USER_MODEL = 'users.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'mozilla_django_oidc.middleware.SessionRefresh',
]
AUTHENTICATION_BACKENDS = [
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
    # 'users.backends.CustomOIDCAuthenticationBackend',
]

# AUTHENTICATION_BACKENDS = (
#     'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )

ROOT_URLCONF = 'patientordersystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'patientordersystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Auth0 Credentials
OIDC_RP_CLIENT_ID = "loHB9FWuTUICrN5iIhY2O1MZSwcK93KX"
OIDC_RP_CLIENT_SECRET = "DdXWvsuXt9i4jJp7Y15quX2WSDauqP18cAXG_S30ZOnp8nJRyYNmPorpTMGH6wDo"
OIDC_OP_DOMAIN = "dev-ytcq356n3j8xg643.eu.auth0.com"



OIDC_OP_AUTHORIZATION_ENDPOINT = 'https://dev-ytcq356n3j8xg643.eu.auth0.com/authorize'
OIDC_OP_TOKEN_ENDPOINT = 'https://dev-ytcq356n3j8xg643.eu.auth0.com/oauth/token'
OIDC_OP_USER_ENDPOINT = 'https://dev-ytcq356n3j8xg643.eu.auth0.com/userinfo'
OIDC_OP_JWKS_ENDPOINT = 'https://dev-ytcq356n3j8xg643.eu.auth0.com/.well-known/jwks.json'
OIDC_RP_SIGN_ALGO = 'RS256'
# OIDC_RP_REDIRECT_URI = 'http://localhost:8000/oidc/callback/'
# OIDC_STORE_ACCESS_TOKEN = True  # Store access tokens for API calls if needed
# OIDC_STORE_ID_TOKEN = True
# OIDC_STATE_TIMEOUT = 600   

# SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = False
# OIDC_RP_CLIENT_ID = "TqfmixiJHrkg33Z2IauKIoXOMHMtIxQw"
# OIDC_RP_CLIENT_SECRET = "tX7gJMC7v9c0XY5zHkJKfx9aF6K8XvQc7ytVOPSfieLo3bq_4BhCzPvLoZ96cnfd"
# OIDC_OP_DOMAIN = "dev-ytcq356n3j8xg643.eu.auth0.com"

# # OpenID Connect Settings
# OIDC_OP_AUTHORIZATION_ENDPOINT = f"https://{OIDC_OP_DOMAIN}/authorize"
# OIDC_OP_TOKEN_ENDPOINT = f"https://{OIDC_OP_DOMAIN}/oauth/token"
# OIDC_OP_USER_ENDPOINT = f"https://{OIDC_OP_DOMAIN}/userinfo"
# OIDC_RP_SIGN_ALGO = "RS256"
# OIDC_STORE_ACCESS_TOKEN = True  # Store access tokens for API calls if needed
# OIDC_STORE_ID_TOKEN = True      # Store ID tokens if you want to use them

# SIMPLE_JWT = {
#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
#     'ALGORITHM': 'RS256',
#     'SIGNING_KEY': None,  # Set as None since it will use a verifying key instead
#     'VERIFYING_KEY': None,  # Can leave as None if using JWK_URL
#     'AUDIENCE': 'https://patientorder.com/api/v3/',  # Replace with your Auth0 API Audience
#     'ISSUER': 'https://dev-ytcq356n3j8xg643.eu.auth0.com/',  # Replace with your Auth0 domain
#     'JWK_URL': 'https://dev-ytcq356n3j8xg643.eu.auth0.com/.well-known/jwks.json',
# }

# SIMPLE_JWT = {
#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),  # Adjust as needed
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
#     'ALGORITHM': 'RS256',
#     'AUDIENCE': 'https://dev-ytcq356n3j8xg643.eu.auth0.com/api/v2/',  # Simplify audience path if possible
#     'ISSUER': 'https://dev-ytcq356n3j8xg643.eu.auth0.com/',
#     'JWK_URL': 'https://dev-ytcq356n3j8xg643.eu.auth0.com/.well-known/jwks.json',
# }

# AUTHLIB_OAUTH_CLIENTS = {
#     'auth0': {
#         'client_id': OIDC_RP_CLIENT_ID,           # From Auth0 Application settings
#         'client_secret': OIDC_RP_CLIENT_SECRET,    # From Auth0 Application settings
#         'server_metadata_url': f"https://{OIDC_OP_DOMAIN}/.well-known/openid-configuration",
#         'authorize_url': f"https://{OIDC_OP_DOMAIN}/authorize",
#         'access_token_url': f"https://{OIDC_OP_DOMAIN}/oauth/token",
#         'userinfo_url': f"https://{OIDC_OP_DOMAIN}/userinfo",
#         'client_kwargs': {
#             'scope': 'openid profile email',
#         },
#     }
# }

# Specify the login URL for redirection if unauthenticated
LOGIN_URL = '/oidc/login/'
LOGOUT_URL = "/oidc/logout/"
LOGIN_REDIRECT_URL = '/'  # Or any page you prefer
LOGOUT_REDIRECT_URL = '/'
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

AFRICASTALKING_USERNAME = 'klausorioki'
AFRICASTALKING_API_KEY = 'atsk_d58a80a4050843a4af2c5b5743eee9823a8b37add422a780f6a7c27750873a531ad773f2'

# AFRICASTALKING_USERNAME = 'sandbox'
# AFRICASTALKING_API_KEY = 'atsk_942109f5e2d58376e18a01c8f5542ed27c52036e168e7e0be878c2fc136355f61adf4c10'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
