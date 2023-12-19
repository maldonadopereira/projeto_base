from pathlib import Path
from decouple import Csv, config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ROOT_URLCONF = 'projeto.urls'


WSGI_APPLICATION = 'projeto.wsgi.application'

INTERNAL_IPS = config('INTERNAL_IPS', cast=Csv(), default='127.0.0.1')
