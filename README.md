# [Django_ECommerce_Demo](https://www.jerryyu.click) 

  This project is a demo e-commerce website built with Django, Bootstrap, PostgreSQL, Celery, Redis, uwsgi and Nginx. The whole project was containerized by Docker and deployed on AWS EC2.

## Information
- Website URL: [https://www.jerryyu.click](https://www.jerryyu.click) 

- Root User : admin
- Password : admin

- Credit Card : 4311-9522-2222-2222</br>
- Date : 12/22</br>
- CVV : 222</br>

## Django ORM Schema
![image](https://bnz05pap001files.storage.live.com/y4mPTzVeh7LOK-9S9sNQf5DqHV6epvcp-W64Dx7hRbO2IuM5r1GRGdVEhE4wvyzA2axZCDYXJ6we3ZyY3VYEaE-q9dRcUROM-Cuj7USuyzL3ofMfxPBsqBsSFyVYCanppv24b3xBMXH8Lti7_MQpRnOgG7WFmMnEtyJedy8xN2hBf4UF5Dg1Ssk-dzB-OxT33Xy?width=660&height=592&cropmode=none)
## Backend Architecture
![image](https://bnz05pap001files.storage.live.com/y4m8hqpr2Un8a7J8OEJcpolmPJfiDx1g-asKAfTI6QHA6UE4GkOkC3XDgKxM-MBBQAcc4XR961OjshhwzX6k3b0pTbYvXzHI1QcF-mf_CASABJa_kcLUUYrXfkpXcdjTmFLlF8hgWMAXeppqsBo4s5F3ZLvC8vKHe1BSlVnA9k2YubgaI_mDyjfHsREmX0U7d89?width=1024&height=344&cropmode=none)
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
ECPay
  ![image](https://raw.githubusercontent.com/jeyu54217/Django_ECommerce_Demo/main/Demo/static/images/demo/demo_ECPay.jpg)
Order Success email
  ![image](https://bnz05pap001files.storage.live.com/y4mszs4b_gnV-lMhQ0aLuRfDgvyvPQ9hYSS8zCLqnSgSE3RYBlEpPYyydnbSI8mnxjcBgdpl7zNeNXCUMOUwRIWrDCMQtGLEsAGCsRF6N_oJUqyYMGcpYr_gCtAIkqGfkrSJaWfCvElMm_9ah_1m-C63LknNGxlQam1m6Vp0-gcKcJshw_4QcGSIHklVDmCP0sP?width=660&height=330&cropmode=none)
 
