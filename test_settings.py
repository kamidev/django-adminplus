INSTALLED_APPS = (
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.auth',
    'django.contrib.admin',
    'adminplus',
)

SECRET_KEY = 'adminplus'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    },
}

TEMPLATES = [
            {
                        'BACKEND': 'django.template.backends.django.DjangoTemplates',
                                'APP_DIRS': True,
                                    },
            ]
'context_processors': [
    # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
    # list if you haven't customized them:
    'django.contrib.auth.context_processors.auth',
    'django.template.context_processors.debug',
    'django.template.context_processors.i18n',
    'django.template.context_processors.media',
    'django.template.context_processors.static',
    'django.template.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.request', # <-- Here we add the request
],
	
ROOT_URLCONF = 'test_urlconf'
MIDDLEWARE_CLASSES = ()
