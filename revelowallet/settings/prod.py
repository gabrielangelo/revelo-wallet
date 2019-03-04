from os.path import join, dirname, exists

import environ
import dj_database_url

from .local import *
from core.utils import print_shadow_green

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)  

env_file = join(dirname(__file__), '.env')

if exists(env_file):
    environ.Env.read_env(str(env_file))
    db_from_env = dj_database_url.config(default=env('DATABASE_URL'))
    
    DATABASES['default'].update(db_from_env)

    SECRET_KEY = env('SECRET_KEY')

    ALLOWED_HOSTS = env('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])
     
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    
    MIDDLEWARE += [
        'django.middleware.security.SecurityMiddleware'
    ]
    
    print_shadow_green('app running with production config')
else:
    print_shadow_green('app running with local config')




