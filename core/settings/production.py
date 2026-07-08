from .base import *

DEBUG = False
ALLOWED_HOSTS = ['virginpreps.com', 'www.virginpreps.com', 'srinivasasnature.com', 'www.srinivasasnature.com',]


SECRET_KEY = env('SECRET_KEY')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_NAME', 'yourdb'),
#         'USER': os.environ.get('DB_USER', 'youruser'),
#         'PASSWORD': os.environ.get('DB_PASSWORD', ''),
#         'HOST': os.environ.get('DB_HOST', 'localhost'),
#         'PORT': os.environ.get('DB_PORT', '5432'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    }
}

RAZORPAY_KEY_ID = env("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = env("RAZORPAY_KEY_SECRET")