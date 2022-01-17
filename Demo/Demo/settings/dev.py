from Demo.settings.base import *


ALLOWED_HOSTS = ["*"]
DEBUG = True
STATICFILES_DIRS = ( os.path.join('static'), )
# CSRF protection 
SECRET_KEY = "django-insecure-w1*7y5jovc#xyei65ixy6gc^y*k@^goom^xyh*#55gvbixapti"
# a list of directories where you want collectstatic to look when collecting the static files. If cannot include STATIC_ROOT or any subdirectory of it.
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)


### DBMS for development ###
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

### SMTP-EMAIL ###
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' # SMTP Server
EMAIL_USE_TLS = True          # turn on TLS(傳輸層安全性)
EMAIL_PORT = 587              # TLS PORT
EMAIL_HOST_USER = 'jeyu54217@gmail.com'
EMAIL_HOST_PASSWORD = 'Qeczawdxs321!'
WEBSITE_URL = "demo.com"

### 3-party sign-in ### - Provider settings
Google_Client_ID = '1021279696244-76eiutmeco59hp8mcj9cl4rvqlaa69e0.apps.googleusercontent.com' # API ID
Google_Client_secret = 'f4voLnIPS1fnnDQGfOKfLcm0' 
SITE_ID = 1
SOCIALACCOUNT_PROVIDERS = {                   
    # Dashboard : https://reurl.cc/82da8y
    'google': {
        'APP': {
            'client_id': Google_Client_ID,
            'secret': Google_Client_secret,
        }
    }
}

### CELRY ###

CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'   
CELERY_TIMEZONE = 'Asia/Taipei' 
# Celery & Rabbitmq protocol problem -Received and deleted unknown message : https://reurl.cc/52V1pn
CELERY_TASK_PROTOCOL = 1  
# # When using librabbitmq, must use PROTOCOL 1
# # https://stackoverflow.com/questions/42081061/celery-rabbitmqwarning-mainprocess-received-and-deleted-unknown-message-wron/42561772
# # celery : https://ithelp.ithome.com.tw/articles/10243148?sc=iThomeR
