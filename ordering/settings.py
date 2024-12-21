"""
Django settings for school project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vex3%bq7byz=55)q#c_i3*n0_f90e2g)##xsdpwz=-(_y-wz7+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []




# Application definition

INSTALLED_APPS = [
    #'customer.apps.CustomerConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken', 
    #'myapp',
    'ordering',
    'customer',
    'phonenumber_field',
    'restaurant',
    # 'order',
    # 'menu',
    'delivery',
    'drf_yasg',
    'import_export',
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

ROOT_URLCONF = 'ordering.urls'
LOGOUT_REDIRECT_URL = '/'

# AUTH_USER_MODEL = 'teacher.CustomUser'

#SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [os.path.join(SETTINGS_PATH, 'templates')],
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

WSGI_APPLICATION = 'ordering.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',  # Use mysqlclient
       'NAME': 'food_ordering_db',
       'USER': 'root',
       'PASSWORD': 'root',
       'HOST': 'localhost',
       'PORT': '3306',
   }
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'Enter your token in the format `Token <your-token>`'
        }
    },
    'DEFAULT_INFO': 'ordering.api.urls.schema_view',
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = '/static/'

# Point to the exact location of your static files directory
STATICFILES_DIRS = [
    #r"D:\PROJECTS\FOOD-ORDERING\Food-ordering\ordering\static",  # Ensure this points to the correct static directory
    # "static/"
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'my_files')

# Static root for collectstatic command
#STATIC_ROOT = r"D:\PROJECTS\FOOD-ORDERING\Food-ordering\ordering"  # This is where collectstatic will gather all static files for production
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'customer.CustomUser'

LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = 'login'

MEDIA_ROOT = BASE_DIR /'media'

MEDIA_URL = '/media/'
