from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/
SECRET_KEY = 'django-insecure-8!alj=*vvvt(qs3isu4e_u&odksqanv)^akdr6hity3k1k=c#$'
DEBUG = True
ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1', '*.ngrok-free.app', '103.173.255.165']

# Application definition
INSTALLED_APPS = [
    'ui.admin_apps.MyAdminConfig',  # Chỉ khai báo MyAdminConfig
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ui',
    'ckeditor',
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

ROOT_URLCONF = 'ravi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'ravi.wsgi.application'

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'static/media'

if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static', 
    ]
else:
    STATIC_ROOT = BASE_DIR / 'media/static'

# CKEditor settings
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js' 
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'width': 'auto',
        'extraPlugins': ','.join(['codesnippet']),
    },
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ALLOW_UNICODE_SLUGS = True

# Admin Reorder settings
ADMIN_REORDER = (
    {'app': 'ui', 'label': 'Quản lý Media', 'models': ['Banner']},
    {'app': 'ui', 'label': 'Về chúng tôi', 'models': ['AboutMe']},
    {'app': 'ui', 'label': 'Lĩnh vực hoạt động', 'models': ['Action', 'ItemAction']},
    {'app': 'ui', 'label': 'Dự án', 'models': ['Project', 'ItemProject']},
    {'app': 'ui', 'label': 'Tuyển dụng', 'models': ['Recruitment', 'NameItemRecruitment']},
    {'app': 'ui', 'label': 'Đối tác', 'models': ['Partner', 'ItemPartner']},
    {'app': 'ui', 'label': 'Đăng ký', 'models': ['Register']},
    {'app': 'ui', 'label': 'Khu vực', 'models': ['Area']},
)
