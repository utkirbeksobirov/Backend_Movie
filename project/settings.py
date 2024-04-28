from .cdn.conf import DEFAULT_FILE_STORAGE, STATICFILES_STORAGE
from pathlib import Path
from datetime import timedelta
import os
from dotenv import load_dotenv
import boto3

BASE_DIR = Path(__file__).resolve().parent.parent


load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
WEBSITE_URL = os.environ.get('WEBSITE_URL')


# Application definition
#1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # install apps
    'main_app',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'storages',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ALLOW_ALL_ORIGINS = True

SITE_ID = 1

SESSION_COOKIE_DOMAIN = WEBSITE_URL

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True

SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True


CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'project.urls'
BASE_DIR = Path(__file__).resolve().parent.parent
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DATABASE_NAME"), 
        'USER': os.getenv("DATABASE_USER"),
        'PASSWORD': os.getenv("DATABASE_PASSWORD"),
        'HOST': os.getenv("DATABASE_HOST"),
        'PORT': os.getenv("DATABASE_PORT"),
        'sslmode': os.getenv("DATABASE_SSL"),
   }
}




# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'






# MEDIAFILES_DIRS = [
#     os.path.join(BASE_DIR, "media"),
# ]

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ENABLED = True
AWS_S3_SECURE_URLS = True


DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 3000
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 3000

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_SIGNATURE_NAME = os.getenv("AWS_S3_SIGNATURE_NAME")
AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")
AWS_S3_FILE_OVERWRITE = os.getenv("AWS_S3_FILE_OVERWRITE")
AWS_DEFAULT_ACL = os.getenv("AWS_DEFAULT_ACL")
AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")
AWS_S3_CUSTOM_DOMAIN = "%s.s3.ap-southeast-1.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
AWS_S3_VERIFY = os.getenv("AWS_S3_VERIFY")
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_QUERYSTRING_EXPIRE = os.getenv("AWS_QUERYSTRING_EXPIRE")



STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = 'https://%s.s3.ap-southeast-1.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME
# STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = 'https://%s.s3.ap-southeast-1.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
# MEDIA_URL = "/media/"

STATICFILES_STORAGE = STATICFILES_STORAGE
DEFAULT_FILE_STORAGE = DEFAULT_FILE_STORAGE

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:8000',
    'http://localhost:5173',
    'https://movie-frontend-vite.vercel.app',
    'https://movie-backend-4l4oj.ondigitalocean.app',
    
]


CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:5173',
    'https://movie-frontend-vite.vercel.app',
    'https://movie-backend-4l4oj.ondigitalocean.app',
    
]

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:5173',
    'https://movie-frontend-vite.vercel.app',
    'https://movie-backend-4l4oj.ondigitalocean.app',
    
]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    endpoint_url='https://movieitebucket.fra1.digitaloceanspaces.com'
)

# # Ma'lumotlar bazasiga mahsulot rasm fayllarini saqlash uchun funksiya
# def save_product_image(file_name, file_content):
#     """Ma'lumotlar bazasiga mahsulot rasm faylini saqlash"""
#     s3.put_object(Bucket='movieitebucket', Key=file_name, Body=file_content)

# # Mahsulotlar rasm faylini olish uchun funksiya
# def get_product_image_url(file_name):
#     """Mahsulotlar rasm faylini olish"""
#     return f"https://movieitebucket.fra1.digitaloceanspaces.com/{file_name}"
