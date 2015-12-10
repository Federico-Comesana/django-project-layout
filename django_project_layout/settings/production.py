# Fetch our base settings
from base import *

#https://docs.djangoproject.com/en/1.8/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    '.example.com',  # Allow domain and subdomains
    '.example.com.',  # Also allow FQDN and subdomains
]