from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    '*.pythonanywhere.com',
]

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
