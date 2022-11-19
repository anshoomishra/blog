from .base import *
from dotenv import load_dotenv
DEBUG = True

ALLOWED_HOSTS = ["localhost"]
# SECRET_KEY = os.environ["SECRET_KEY"]
load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")

print(__name__,SECRET_KEY)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

