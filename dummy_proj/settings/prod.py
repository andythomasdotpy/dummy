from .base import *

print("prod")

# SECRET_KEY = "django-insecure-v#6tp%xx)vs*3iza9l0^8^13p-^lnf$*6f0sfpz6)vf*763!$k"

DEBUG = False

ALLOWED_HOSTS = [
    "anpythomas.com",
    "www.anpythomas.com",
]

# HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS settings
SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True