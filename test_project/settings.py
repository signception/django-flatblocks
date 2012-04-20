import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
#sys.path.insert(0, os.path.dirname(PROJECT_ROOT))

DEBUG=True
TEMPLATE_DEBUG=True
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/flatblocks.db'
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'flatblocks',
    'south'
)
LANGUAGES = (
    ('en-us', 'English'),
    ('de', 'German'),
    ('es', 'Spanish'),
)
LANGUAGE_CODE = 'en-us'
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)
ROOT_URLCONF = 'test_project.urls'
SITE_ID=1
