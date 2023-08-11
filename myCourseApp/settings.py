"""
Django settings for myCourseApp project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from azure.storage.blob import AzureBlobStorage


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o5*+)0l)h-$fzbbksxhu8bpsva7$d0j-6p+oqh-c($25+p97iv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['c2063081.azurewebsites.net']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'modules.apps.ModulesConfig',
    'users.apps.UsersConfig',
    
    
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

ROOT_URLCONF = 'myCourseApp.urls'

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

WSGI_APPLICATION = 'myCourseApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moduleapp',
        'USER': 'c2063081',     
        'PASSWORD': 'June0620@', 
        'HOST': 'c2063081.mysql.database.azure.com',  
        'PORT': '3306',                
        'OPTIONS': {
            'ssl': {
                'ca': 'DigiCertGlobalRootCA.crt.pem',  # Path to your CA certificate file
            },
        },
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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Azure Blob Storage configurations
AZURE_ACCOUNT_NAME = 'c2063081'
AZURE_ACCOUNT_KEY = 'Ce8GO0ugoRfwDfGgE12t9gmwdJt7fUQquK00mQD57Xm00PSMSBY1jJwAel5dqDaWjp3nJ3b1SjVd+AStLO6D1A=='
AZURE_MEDIA_CONTAINER = 'media'
AZURE_STATIC_CONTAINER = 'static'


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'https://' + AZURE_ACCOUNT_NAME + '.blob.core.windows.net/' + AZURE_STATIC_CONTAINER + '/'
STATICFILES_STORAGE = 'myCourseApp.storage.AzureStaticStorage'

# Use Azure Blob Storage for serving media files
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'https://' + AZURE_ACCOUNT_NAME + '.blob.core.windows.net/' + AZURE_MEDIA_CONTAINER + '/'
DEFAULT_FILE_STORAGE = 'myCourseApp.storage.AzureMediaStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_ALLOWED_TEMPLATE_PACK = 'bootstrap4'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = 'modules:home'
LOGIN_URL = 'login'
