import os
from sendgrid import SendGridAPIClient
from django.conf import settings
from sendgrid.helpers.mail import Mail
from django.template.loader import render_to_string

def send_mail(user,e_body):
    print(settings.SENDGRID_API_KEY)
    context={
        'user': user,
        'e_body': e_body,
    }
    msg_html = render_to_string('email.html',context)
    message = Mail(
        from_email='gkilewa1@gmail.com',
        to_emails=[user.email],
        subject='Cavaliers HRM Account verification',
        html_content= msg_html)
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(e)