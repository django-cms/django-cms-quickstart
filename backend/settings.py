from pathlib import Path
import os
import dj_database_url
from django_storage_url import dsn_configured_storage_class

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '<a string of random characters>')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG') == "True"

ALLOWED_HOSTS = [os.environ.get('DOMAIN'),]
if DEBUG:
    ALLOWED_HOSTS = ["*",]

# Redirect to HTTPS by default, unless explicitly disabled
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT') != "False"

X_FRAME_OPTIONS = 'SAMEORIGIN'


# Application definition

INSTALLED_APPS = [
    'backend',

    # optional, but used in most projects
    'djangocms_admin_style',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # key django CMS modules
    'cms',
    'menus',
    'treebeard',
    'sekizai',

    # Django Filer - optional, but used in most projects
    'filer',
    'easy_thumbnails',

    # the default publishing implementation - optional, but used in most projects
    'djangocms_versioning',

    # the default alias content - optional, but used in most projects
    'djangocms_alias',
    'parler',

    # links
    'djangocms_link',

    # the next-gen text editor - optional, but used in most projects
    'djangocms_text',

    # optional django CMS frontend modules
    'djangocms_frontend',
    'djangocms_frontend.contrib.accordion',
    'djangocms_frontend.contrib.alert',
    'djangocms_frontend.contrib.badge',
    'djangocms_frontend.contrib.card',
    'djangocms_frontend.contrib.carousel',
    'djangocms_frontend.contrib.collapse',
    'djangocms_frontend.contrib.content',
    'djangocms_frontend.contrib.grid',
    'djangocms_frontend.contrib.jumbotron',
    'djangocms_frontend.contrib.link',
    'djangocms_frontend.contrib.listgroup',
    'djangocms_frontend.contrib.media',
    'djangocms_frontend.contrib.icon',
    'djangocms_frontend.contrib.image',
    'djangocms_frontend.contrib.tabs',
    'djangocms_frontend.contrib.utilities',

    'taggit',
    'taggit_autosuggest',
    'meta',
    'sortedm2m',
    'djangocms_blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'django.template.context_processors.i18n',

                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',

            ],
        },
    },
]

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

CMS_TEMPLATES = [
    # Default template that extend base.html, to be used with Bootstrap 5
    ('bootstrap5.html', 'Bootstrap 5 Demo'),

    # a minimal template to get started with
    ('minimal.html', 'Minimal template'),

    ('whitenoise-static-files-demo.html', 'Static File Demo'),
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# Configure database using DATABASE_URL; fall back to sqlite in memory when no
# environment variable is available, e.g. during Docker build
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite://:memory:')
DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

if not DEBUG:
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

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', 'English'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_DIRS = [  # this are were django staticfiles is looking for sources
    BASE_DIR / "backend" / "static",
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_collected')  # this is were the collected files are placed

# read the setting value from the environment variable. This functionality is
# provided by https://github.com/divio/django-storage-url
DEFAULT_STORAGE_DSN = os.environ.get('DEFAULT_STORAGE_DSN', '/data/media/')
DefaultStorageClass = dsn_configured_storage_class('DEFAULT_STORAGE_DSN')

STORAGES = {
    'default': {
        'BACKEND': 'backend.settings.DefaultStorageClass',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
        # 'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    },
}

# only required for local file storage and serving, in development
MEDIA_URL = 'media/'
MEDIA_ROOT = '/data/media/'


SITE_ID = 1

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

CMS_CONFIRM_VERSION4 = True
DJANGOCMS_VERSIONING_ALLOW_DELETING_VERSIONS = True
