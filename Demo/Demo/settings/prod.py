from Demo.settings.base import *

DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ['*']  

SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = True

# An absolute path where Django puts the static files that are collected using collectstatic. 
# Where your web server will serve static files from this directory.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# For E-mail URL & ECPay return URL
WEBSITE_URL = os.environ.get("WEBSITE_URL")

### DBMS for Deployment ###
DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql',
        "NAME": os.environ.get("PSQL_DATABASE",),
        "USER": os.environ.get("PSQL_USER",),
        "PASSWORD": os.environ.get("PSQL_PASSWORD",),
        "HOST": os.environ.get("PSQL_HOST",),
        "PORT": os.environ.get("PSQL_PORT",5432),
    }
}

### allauth 3rd-Party Login setting- Provider ###
SITE_ID = 1
SOCIALACCOUNT_PROVIDERS = {                   
    # google API Dashboard : https://reurl.cc/82da8y
    'google': {
        'APP': {
            'client_id': os.environ.get("Google_Client_ID",),
            'secret': os.environ.get("Google_Client_secret",),
        }
    }
}

### SMTP-EMAIL ###
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' # SMTP Server
EMAIL_USE_TLS = True          
EMAIL_PORT = 587              
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")


### CELRY ###
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
# CELERY_RESULT_BACKEND ='amqp://guest:guest@localhost:5672//'
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'   
CELERY_TIMEZONE = 'Asia/Taipei' 
# Celery & Rabbitmq protocol problem -Received and deleted unknown message : https://reurl.cc/52V1pn
CELERY_TASK_PROTOCOL = 1  
# When using librabbitmq, must use PROTOCOL 1
# https://stackoverflow.com/questions/42081061/celery-rabbitmqwarning-mainprocess-received-and-deleted-unknown-message-wron/42561772
# celery : https://ithelp.ithome.com.tw/articles/10243148?sc=iThomeR
# about localhost in docker : https://stackoverflow.com/questions/55410120/docker-celery-cannot-connect-to-redis?rq=1