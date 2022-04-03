import os
SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES = {
      'default': {
        'CONNECTION_STRING': os.getenv('CONNECTION_STRING'),
        'DB_NAME': os.getenv('DB_NAME'),
    }
}