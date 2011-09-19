from django.conf import settings

MIDDLEWARE_CLASSES = getattr(settings, 'MIDDLEWARE_CLASSES', {})
LANGUAGE_CODE = getattr(settings, 'LANGUAGE_CODE', 'en')
CACHE_PREFIX = getattr(settings, 'FLATBLOCKS_CACHE_PREFIX', 'flatblocks_')
AUTOCREATE_STATIC_BLOCKS = getattr(settings,
    'FLATBLOCKS_AUTOCREATE_STATIC_BLOCKS', False)
