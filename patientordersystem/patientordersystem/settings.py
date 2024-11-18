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
import dj_database_url
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-eubv%df3ic(@!9)_ctsg^9svwtj*%=c_cfi^qvzs@7awn^vcv4'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get('DEBUG', "False").lower() = 'true'

DEBUG = True 

# ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(" ")

ALLOWED_HOSTS= [ '127.0.0.1:8000', 'localhost:8000', '127.0.0.1', 'localhost', 'savannah-patient-order-service.onrender.com' ]



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

ROOT_URLCONF = 'patientordersystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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
# database_url = os.environ.get("DATABASE_URL")
# DATABASES['default'] = dj_database_url.parse('database_url')

# DATABASES['default'] = dj_database_url.parse("postgresql://patient_order_database_user:lj9bHkuNZO2w7vM6TDj1pIHADDIqC8f2@dpg-cstm0sm8ii6s73fkeem0-a.frankfurt-postgres.render.com/patient_order_database")
DATABASES['default'] = dj_database_url.parse("postgresql://patient_order_database_user:lj9bHkuNZO2w7vM6TDj1pIHADDIqC8f2@dpg-cstm0sm8ii6s73fkeem0-a/patient_order_database")
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

# OIDC_RP_CLIENT_ID = os.environ.get("OIDC_RP_CLIENT_ID")
# OIDC_RP_CLIENT_SECRET = os.environ.get("OIDC_RP_CLIENT_SECRET")
# OIDC_OP_DOMAIN = os.environ.get("OIDC_OP_DOMAIN")

OIDC_OP_AUTHORIZATION_ENDPOINT = f"https://{OIDC_OP_DOMAIN}/authorize"
OIDC_OP_TOKEN_ENDPOINT = f"https://{OIDC_OP_DOMAIN}/oauth/token"
OIDC_OP_USER_ENDPOINT = f"https://{OIDC_OP_DOMAIN}/userinfo"
OIDC_OP_JWKS_ENDPOINT = f"https://{OIDC_OP_DOMAIN}/.well-known/jwks.json"
OIDC_RP_SIGN_ALGO = 'RS256'
# OIDC_RP_REDIRECT_URI = 'http://localhost:8000/oidc/callback/'
# OIDC_STORE_ACCESS_TOKEN = True  # Store access tokens for API calls if needed
# OIDC_STORE_ID_TOKEN = True
# OIDC_STATE_TIMEOUT = 600   

# SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = False


# AFRICASTALKING_USERNAME = 'klausorioki'
# AFRICASTALKING_API_KEY = 'atsk_d58a80a4050843a4af2c5b5743eee9823a8b37add422a780f6a7c27750873a531ad773f2'

AFRICASTALKING_USERNAME = 'sandbox'
AFRICASTALKING_API_KEY = 'atsk_942109f5e2d58376e18a01c8f5542ed27c52036e168e7e0be878c2fc136355f61adf4c10'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# LOGIN_URL = '/oidc/login/'
# LOGOUT_URL = "/oidc/logout/"
# LOGIN_REDIRECT_URL = '/'  # Or any page you prefer
# LOGOUT_REDIRECT_URL = '/'

LOGIN_URL = '/oidc/login/'
LOGIN_REDIRECT_URL = '/authenticated/'  # Redirect to AuthenticatedHomeView after login
LOGOUT_REDIRECT_URL = '/'  # Redirect to HomeView after logout

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / "static"]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
