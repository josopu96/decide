ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

APIS = {
    'authentication': 'localhost',
    'base': 'localhost',
    'booth': 'localhost',
    'census': 'localhost',
    'mixnet': 'localhost',
    'postproc': 'localhost',
    'store': 'localhost',
    'visualizer': 'localhost',
    'voting': 'localhost',
}

BASEURL = 'localhost'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
