# [Django_ECommerce_Demo](https://www.jerryyu.click) 

  This project is a demo ECommerce website built with Django, Bootstrap, PostgreSQL, Celery, Redis, uwsgi, Nginx, and so on. The whole project was containerized by Docker and deployed on AWS EC2.

## Information
- Website URL: [https://www.jerryyu.click](https://www.jerryyu.click) 

- Root User : admin
- Password : admin

- Credit Card : 4311-9522-2222-2222</br>
- Date : 12/22</br>
- CVV : 222</br>


## Techniques & Tools
* Frontend:
    - [Bootstrap (5.1)](https://getbootstrap.com/)
* Backend:
    - Framework
        - [Django (3.2)](https://www.djangoproject.com/)
            - MVT design pattern
            - [session](https://docs.djangoproject.com/en/4.0/topics/http/sessions/)
            - [form](https://docs.djangoproject.com/en/4.0/topics/forms/)
            - [email](https://docs.djangoproject.com/en/4.0/topics/email/)
            - [admin](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/)
            - [alluth (Google)](https://django-allauth.readthedocs.io/en/latest/index.html)
    - Asynchronous Tasks
        - [Celery](http://www.celeryproject.org/)
    - Cache:
        - [Redis](https://redis.io/)
    - RDBMS:
        - [PostgreSQL](https://www.postgresql.org/)
    - 3rd Party Payment
        - [ECPay](https://www.ecpay.com.tw/Service/API_Dwnld)
* Deployment:
    - [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)
    - [NGINX](https://nginx.org/en/)
    - [Docker](https://www.docker.com/)
        - [freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/#)
        - [Docker-compose](https://docs.docker.com/compose/)
    - [AWS](https://aws.amazon.com/)
        - EC2
        - ALB 
        - Route 53 (DNS)
        - Certificate Manager (SSL)
## References
   - Internet
        - [[Book] James Kurose, Keith Ross (2016). Computer Networking: A Top-Down Approach 7th](https://www.amazon.com/Computer-Networking-Top-Down-Approach-7th/dp/0133594149)
        - [[Book] 井上直也, 村山公保, 竹下隆史, 荒井透, 苅田幸雄  (2021). 圖解TCP/IP網路通訊協定（涵蓋IPv6）2021修訂版](https://www.books.com.tw/products/0010883910?sloc=main)
   - Python
        - [[Udemy] Colt Steele (2020).Ultimate AWS Certified Developer Associate ](https://www.udemy.com/course/the-modern-python3-bootcamp/)
        - [[Book] Bill Lubanovic (2019).Introducing Python, 2nd Edition](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/)
   - Frontend
        - [[Udemy] Angela Yu (2020). The Complete 2020 Web Development Bootcamp](https://www.udemy.com/course/the-complete-web-development-bootcamp/)
   - Django
        - [[Book] Antonio Melé (2018). Django 2 by Example: Build powerful and reliable Python web applications from scratch ](https://www.amazon.com/Django-Example-powerful-reliable-applications/dp/1788472489)
            - [Django2实战示例](https://www.cnblogs.com/superhin/p/13223588.html)
    - Docker:
        - [[Youtube] Mumshad Mannambeth, KodeKloud (2021). Docker Tutorial for Beginners - A Full DevOps Course on How to Run Applications in Containers](https://www.youtube.com/watch?v=zJ6WbK9zFpI)
        - [[Youtube] TechWorld with Nana (2021). Docker Tutorial for Beginners ](https://www.youtube.com/watch?v=3c-iBn73dDE)
        - [[Youtube] London App Developer (2021). Deploying Django with Docker Compose](https://www.youtube.com/watch?v=mScd-Pc_pX0)
    - AWS:
        - [[Udemy] Stephane Maarek (2021). Ultimate AWS Certified Developer Associate ](https://www.udemy.com/course/aws-certified-developer-associate-dva-c01/)


## Functions

### Homepage

  ![image](https://raw.githubusercontent.com/jeyu54217/Django_ECommerce_Demo/main/Demo/static/images/demo/demo_home.jpg)
  ![image](https://raw.githubusercontent.com/jeyu54217/Django_ECommerce_Demo/main/Demo/static/images/demo/demo_footer.jpg)

### Authentication
- Sign Up
![image](https://raw.githubusercontent.com/jeyu54217/Django_ECommerce_Demo/main/Demo/static/images/demo/demo_signup.jpg)
- Log In & 3rd Party Log In
![image](https://raw.githubusercontent.com/jeyu54217/Django_ECommerce_Demo/main/Demo/static/images/demo/demo_login.jpg)
- Log out
![image](https://raw.githubusercontent.com/jeyu54217/Django_ECommerce_Demo/main/Demo/static/images/demo/demo_logout.jpg)

### Product Search
  ![image](https://raw.githubusercontent.com/jeyu54217/Django_ECommerce_Demo/main/Demo/static/images/demo/demo_search.jpg)

### Product Page
  ![image](https://raw.githubusercontent.com/jeyu54217/Django_ECommerce_Demo/main/Demo/static/images/demo/demo_product.jpg)

  ![image](https://raw.githubusercontent.com/jeyu54217/Django_ECommerce_Demo/main/Demo/static/images/demo/demo_product2.jpg)

### Cart

  ![image](https://raw.githubusercontent.com/jeyu54217/Django_ECommerce_Demo/main/Demo/static/images/demo/demo_cart.jpg)

  ![image](https://raw.githubusercontent.com/jeyu54217/Django_ECommerce_Demo/main/Demo/static/images/demo/demo_cart2.jpg)

### Order

  ![image](https://raw.githubusercontent.com/jeyu54217/Django_ECommerce_Demo/main/Demo/static/images/demo/demo_checkout.jpg)
  
- ECPay
  ![image](https://raw.githubusercontent.com/jeyu54217/Django_ECommerce_Demo/main/Demo/static/images/demo/demo_ECPay.jpg)

- Succsee e-mail
  ![image](https://raw.githubusercontent.com/jeyu54217/Django_ECommerce_Demo/main/Demo/static/images/demo/demo_success mail.jpg)

