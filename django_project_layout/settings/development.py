# Import some utility functions
from os.path import join
# Fetch our base settings
from base import *

# #########################################################

# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(PROJECT_ROOT, 'run', 'dev.sqlite3'),
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      
        'PORT': '', # Set to empty string for default.
    }
}

# ##### APPLICATION CONFIGURATION #########################

CUSTOM_APPS = [
    #'django_extensions',
    #'reversion',
    #'debug_toolbar',
]

INSTALLED_APPS = DEFAULT_APPS + CUSTOM_APPS
