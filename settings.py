# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres', #MzA2NjctZGF2aWRv
        'PASSWORD': 'Place with your password generated in Step 1',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS = (
    'standalone',
)

SECRET_KEY = 'SECRET KEY for this Django Project'