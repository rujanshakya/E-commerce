"""
Django settings for Handicraft_Nepal project.

Generated by 'django-admin startproject' using Django 3.1.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '338pc(job2%$(@2kdxe+n%m6a^13ojm7u@^#i&+2%9#ko0xblz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'stripe',
    'crispy_forms'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Handicraft_Nepal.urls'

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
                'store.context_processors.menu_links',
                'store.context_processors.counter',

            ],
        },
    },
]

WSGI_APPLICATION = 'Handicraft_Nepal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIRS=[ os.path.join(BASE_DIR,'static')]

#Media directory to store uploaded photos
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'static','media')

STRIPE_PUBLISHABLE_KEY='pk_test_51KXhFiCSThRBLq0jL9GBz5O3Zj4CL1sJKDugOUWEXi3NhPeTfvTv38ILVd8UDdDbuHOlnvByLwDtygrvBygCT0PI005HFAtLqC'
STRIPE_SECRET_KEY='sk_test_51KXhFiCSThRBLq0j7bJKw8sM4JaZ4PmYQmq6GHaC6nWZnFfKUhrfTiEHH2aukJRVeBhQ9MsmgEKxBQtdwxF9nDsn00DFBdmSgY'

CRISPY_TEMPLATE_PACK='bootstrap4'

# EMAIL_HOST = 'smtp.mailgun.org'
# EMAIL_PORT= 587
# EMAIL_USE_TLS= True
# EMAIL_HOST_USER = 'postmaster@sandboxc94cbf7620544786bc3f212dc272de21.mailgun.org'
# EMAIL_HOST_PASSWORD = '81b072414bddf9caeaa1e42e94ab43b9-162d1f80-beb4499a'

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER="handicraftnepal12@gmail.com"
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_PASSWORD="test123@"