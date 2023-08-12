from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def send_email_html(subject, recipient_email, html_message):
    sender_email = settings.EMAIL_HOST_USER
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=sender_email,
        to=recipient_email,
    )
    email.content_subtype = 'html'
    email.send()

def send_email_simple(subject, message, recipient_email):
    sender_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, sender_email, recipient_email)       