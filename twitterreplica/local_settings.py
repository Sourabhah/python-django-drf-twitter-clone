SECRET_KEY = 'django-insecure-$2p@vcgr#n!7i1wgu-x-n5bur91u7wk3ai%a4u%4)#x+as6$k3'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'tweets',

        'USER': 'usertest',

        'PASSWORD': 'pwtest',

        'HOST': 'localhost',

        'PORT': '5432',
    }
}
