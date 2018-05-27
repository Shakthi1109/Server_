from .base import *
import os



DEBUG= True

DATABASES = {
     'default': {

        'NAME': 'ideahub',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'ashutoshverma',
        'PASSWORD': '',
        'HOST' : 'localhost',
        'PORT' :'5432',
    }
}
