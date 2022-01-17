from celery import app 
from django.core.mail import EmailMultiAlternatives
# from orders.models import Order_Info
from django.conf import settings
from django.template.loader import get_template


@app.shared_task
def send_email(recipient_email,): 
    subject = 'Registration Confirmation Email - Django Demo - Jerry Yu'
    template = get_template('account/mail_signup.html')
    template_tag = {
        'WEBSITE_URL': settings.WEBSITE_URL,
    }
    html_content = template.render(template_tag)
    message = ''
    msg = EmailMultiAlternatives(
        subject, 
        message, 
        settings.EMAIL_HOST_USER, 
        [recipient_email]
        )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
            

# EmailMultiAlternatives : Sending alternative content types : https://docs.djangoproject.com/en/3.2/topics/email/#sending-alternative-content-types