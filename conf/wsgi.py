import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

from .env import SETTINGS


os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS)

application = get_wsgi_application()
application = DjangoWhiteNoise(application)