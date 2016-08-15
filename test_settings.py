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

ROOT_URLCONF = 'test_urlconf'
MIDDLEWARE_CLASSES = ()
