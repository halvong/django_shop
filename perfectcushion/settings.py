import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#'/home/hal/Documents/projects/visual_code/Django/ecommerce/perfectcushion'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'u46hs(at+b1da1#jqw&+jqpw20(7imddf0i87xvil2x*25x!b_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stripe',
    'cart',
    'shop',
    'search_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'perfectcushion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'/home/hal/Documents/projects/visual_code/Django/ecommerce/perfectcushion/shop/templates/'
        'DIRS': [
                 os.path.join(BASE_DIR, 'shop', 'templates/'),
                 os.path.join(BASE_DIR, 'cart', 'templates/'),
                 os.path.join(BASE_DIR, 'search_app', 'templates/'),
                ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shop.context_processors.menu_links',
                'cart.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'perfectcushion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shop',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'database',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

#/home/hal/Documents/projects/visual_code/Django/ecommerce/perfectcushion/staticfiles
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#'/home/hal/Documents/projects/visual_code/Django/ecommerce/perfectcushion/static'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
#/home/hal/Documents/projects/visual_code/Django/ecommerce/perfectcushion/static/media
MEDIA_ROOT = os.path.join(BASE_DIR, 'static','media')

STRIPE_PUBLISHABLE_KEY = 'pk_test_NHaWScNKrBj7SNURMwdIeaYF'
STRIPE_SECRET_KEY = 'sk_test_kbcSQGO1FXbEaPjUtVaCPBEC'