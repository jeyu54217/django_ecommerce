# [Django_ECommerce_Demo](https://www.jerryyu.click) 

This project is a demo ECommerce website built with Django, Bootstrap, PostgreSQL, Celery, Redis, uwsgi, Nginx, and so on. The whole project was containerized by Docker and deployed on AWS EC2.

## Info
- Website URL: [https://www.jerryyu.click](https://www.jerryyu.click) 

- Root User : admin
- Password : admin

- Credit Card for Test : 4311-9522-2222-2222</br>
- Date : 12/22</br>
- CVV : 222</br>


## Techniques & tools

* RESTful API架構實踐專案功能

* 使用index加速MySQL查詢效率

* 專案建構於EC2
* 申請SSL憑證實踐HTTPS
### Frontend:
    - [Bootstrap (5)](https://getbootstrap.com/)
### Backend:
    * Framwork
        - [Django (3.2)](https://www.djangoproject.com/)
            - MVT design pattern
            - [session](https://docs.djangoproject.com/en/4.0/topics/http/sessions/)
            - [form](https://docs.djangoproject.com/en/4.0/topics/forms/)
            - [email](https://docs.djangoproject.com/en/4.0/topics/email/)
            - [admin](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/)
            - [alluth (Google)](https://django-allauth.readthedocs.io/en/latest/index.html)
    * Asynchronous Tasks
        - [Celery](http://www.celeryproject.org/)
    * Cache:
        - [Redis](https://redis.io/)
    * RDBMS:
        - [PostgreSQL](https://www.postgresql.org//)
### Deployment:
    - [AWS](https://aws.amazon.com/tw/)
    - [Docker](https://www.docker.com/)
    - [NGINX](https://nginx.org/en/)
    - [Certbot (Let's encryp)](https://certbot.eff.org/)

- Reference:
    - [shopping site (中文)](https://kknews.cc/zh-tw/code/pe9o3x8.html)
    - [Sign in with social media accounts](https://scotch.io/tutorials/django-authentication-with-facebook-instagram-and-linkedin)
    - [twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial](https://github.com/twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial)
    - [Google Analytics - gtagjs](https://developers.google.com/analytics/devguides/collection/gtagjs)

## Functions

### 首頁瀏覽

* 滾輪往下滑，可以閱覽所有景點資訊(1次重新列出12筆新景點)，也可以透過關鍵字搜尋景點標題

  ![image](https://user-images.githubusercontent.com/73434165/121943692-6ba0a780-cd84-11eb-8f04-32423d8a6c28.png)

### 帳號管理

* 使用者可以註冊、登入、登出網站系統

  ![image](https://user-images.githubusercontent.com/73434165/121942693-5b3bfd00-cd83-11eb-864b-a6196c0b8372.png)

* 使用者可以進入各個景點分頁，訂購行程、刪除購物車行程，並在預定行程頁面進行付款

  ![image](https://user-images.githubusercontent.com/73434165/121942891-93434000-cd83-11eb-9651-d4cfcf452185.png)

* 使用者可以在會員系統查看過去的所有歷史訂單，並點選標題超連結進入各個訂購分頁，以及在會員系統進行退款

  ![image](https://user-images.githubusercontent.com/73434165/121943303-051b8980-cd84-11eb-8c63-a664e4179354.png)




- Images: 
    - Homepage  
    ![homepgae](https://raw.githubusercontent.com/jeyu54217/Django_ECommerce_Demo/main/Demo/static/images/demo/demo_home.jpg)
    ![homepgae](https://raw.githubusercontent.com/jeyu54217/Django_ECommerce_Demo/main/Demo/static/images/demo/demo_footer.jpg)
    - Products  
    ![demo_products_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_products_en.png)
    - Product - Coming Soon  (No Image)   
    ![demo_no_image_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_no_image_en.png)
    - Product Detail  
    ![demo_detail_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_detail_en.png)
    - Cart  
    ![demo_carts_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_carts_en.png)
    - Checkout  
    ![demo_checkout_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_checkout_en.png)
    - Sharing  
    ![demo_share_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_share_en.png)
    - Order Confirmation Email  
    ![demo_mail.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_mail.png)
    - Sign In  
    ![demo_3parts_login_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_3parts_login_en.png)
    - Sign In - GitHub  
    ![demo_3parts_login_github_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_3parts_login_github_en.png)
    - Demo Map  
    ![demo_map_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_map_en.png)
    - Google Analytics (GA)
    ![demo_ga.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_ga.png)
    - CloudWatch
    ![cloudWatch.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/cloud_watch.png)

- Functions:
    - Support to:
        - Add goods to shopping cart (recorded by session),
        - Send order confirmation email to customers (Celery + Redis + Gmail),
        - Sign in with third-party accounts (Facebook, Instagram, GitHub),
        - Share to Facebook,
        - View address on Google Map,
        - Manage Categories and Goods in the admin interface.
    - Responsive web design (RWD).
    - Internationalization (i18n).
    - Deployment (AWS + Docker + uWSGI + NGINX + Certbot).
    - Use GA to understand user behavior
- Techniques & tools for building the demo website:
    - Backend:
        - [Django (2.2)](https://www.djangoproject.com/)
            - social-auth-app-django (Facebook, Instagram, GitHub)
            - session
            - form
            - email
            - management
            - i18n
            - test (TODO: finish)
        - [Celery](http://www.celeryproject.org/)
            - [flower](https://flower.readthedocs.io/en/latest/)
    - Frontend:
        - [Bootstrap (4.3)](https://getbootstrap.com/)
        - [Google Analytics (gtag.js)](https://developers.google.com/analytics/devguides/collection/gtagjs)
    - Database:
        - [MySQL](https://www.mysql.com/)
    - Cache:
        - [Redis](https://redis.io/)
    - Deployment:
        - [AWS](https://aws.amazon.com/tw/)
        - [Docker](https://www.docker.com/)
        - [NGINX](https://nginx.org/en/)
        - [Certbot (Let's encryp)](https://certbot.eff.org/)
        - [Jenkins](https://jenkins.io/zh/) (TODO)
- Reference:
    - [shopping site (中文)](https://kknews.cc/zh-tw/code/pe9o3x8.html)
    - [Sign in with social media accounts](https://scotch.io/tutorials/django-authentication-with-facebook-instagram-and-linkedin)
    - [twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial](https://github.com/twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial)
    - [Google Analytics - gtagjs](https://developers.google.com/analytics/devguides/collection/gtagjs)

## Set up
- `cd demo`
- `python3 -m venv venv`
- `. venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py loaddata fixtures/*`
- `python manage.py createsuperuser`
- Add demo/settings/local.py (you can copy [demo/settings/local_example.py](https://github.com/ZoeLiao/python-Django-demo/blob/master/demo/demo/settings/local_example.py) and revise it.) and add your email information, and facebook, instagram, GitHub key (Please read [Send emails](https://github.com/ZoeLiao/python-Django-demo#send-emails) and [Sign in with third-party accounts](https://github.com/ZoeLiao/python-Django-demo#Sign-in-with-third-party-accounts))
- `python manage.py runserver`
- Visit [http://localhost:8000/](http://localhost:8000/)

## Start an app
- If you want to add a new app:
    - `django-admin startapp <app_name>`

## Migrate database
- In general cases:
    - `python manage.py makemigrations`
    - `python manage.py migrate`
- Failed to detect changes:
    - Run the command of [Management - Delete the data of specific app](https://github.com/ZoeLiao/python-Django-demo#management)
    - Fake Migration:
        - Tells Django to mark the migrations as having been applied or unapplied, but without actually running the SQL to change your database schema
        - `python manage.py makemigrations <app_name>`
        - `python manage.py migrate --fake`
    - Migrate:
        - `python manage.py makemigrations <app_name>`
        - `python manage.py migrate`

## Management
- Delete the data of specific app:
    - `python manage.py manual_migration <app_name>`
    - e.g., `python manage.py manual_migration shop`

## Static files
- `python manage.py collectstatic`

## Send emails
- If there is not settings/local.py, create it by `vim demo/settings/local.py` (settings/local.py is an ignored file. (you can copy [demo/settings/local_example.py](https://github.com/ZoeLiao/python-Django-demo/blob/master/demo/demo/settings/local_example.py) and revise it.))
- Input your email information in demo/settings/local.py:
    - `EMAIL_HOST = 'smtp.gmail.com'`
    - `EMAIL_PORT = 587`
    - `EMAIL_HOST_USER = '<your_email>@gmail.com'`
    - `EMAIL_HOST_PASSWORD = '<your_password>'`
- Start Celery by the following command of [Celery - start](https://github.com/ZoeLiao/python-Django-demo#Celery)

## Sign in with third-party accounts:
- If there is not settings/local.py, create it by `vim demo/settings/local.py` (settings/local.py is an ignored file. (you can copy [demo/settings/local_example.py](https://github.com/ZoeLiao/python-Django-demo/blob/master/demo/demo/settings/local_example.py) and revise it.))
- Input your Facebook, Instagram, GitHub key in demo/settings/local.py:
    - Facebook (If you do not have a key, please visit: [facebook for developers](https://developers.facebook.com/docs/facebook-login/web)):
        - `SOCIAL_AUTH_FACEBOOK_KEY = <your Facebook key>`
        - `SOCIAL_AUTH_FACEBOOK_SECRET = <your Facebook secret>`
    - Instagram (If you do not have a key, please visit: [Instagram for developers](https://www.instagram.com/developer/)):
        - `SOCIAL_AUTH_INSTAGRAM_KEY = <your Instagram key>`
        - `SOCIAL_AUTH_INSTAGRAM_SECRET = <your Instagram secret>`
    - GitHub (If you do not have a key, please visit: [GitHub Dveloper](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/)):
        - `SOCIAL_AUTH_GITHUB_KEY = <your GitHub key>`
        - `SOCIAL_AUTH_GITHUB_SECRET = <your GitHub secret>`

## Celery
- Start: `celery -A demo worker -l info`
- Monitor:
    - `celery -A demo flower`
    - Visit [http://localhost:5555](http://localhost:5555)

## Test
- `python manage.py test <app_name>.tests`

## i18n
- `python manage.py makemessages -l <target language>`
    - e.g., `python manage.py makemessages -l zh_Hant`
- `vim demo/locale/<target_language>/LC_MESSAGES/django.po`
    - e.g., `vim demo/locale/zh_Hant/LC_MESSAGES/django.po`
- `python manage.py compilemessages`

## Docker
- `mkdir <path>/sites-available`
- Build: `docker-compose up --build`
- Run: `docker-compose up`
- Remove: `docker-compose down -v`
- docker system prune (-f)
- AWS:
    - `docker-compose up -d`
    - `sudo usermod -a -G docker $USER`
    - sign out and sign in again
    - `sudo service docker start`
- Container:
    - `docker container ls`
    - `docker exec -it <Container ID> bash`

## Deployment
- `docker-compose up --build`
- `docker exec -it <Web Container ID> bash`
- `python manage.py collectstatic`
- `python manage.py createsuperuser`

## Git
- Git doesn't notice change in image:
    - `git rm --cached path/to/image.jpg`
