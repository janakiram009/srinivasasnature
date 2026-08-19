from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
] + MIDDLEWARE

INTERNAL_IPS = [
    "127.0.0.1",
]

# Optional: silence toolbar on AJAX if desired
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: DEBUG,
}