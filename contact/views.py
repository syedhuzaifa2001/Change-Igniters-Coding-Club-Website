from django.shortcuts import render
from .models import Contact
from django.utils import timezone
from django.contrib import messages

# from django.core.mail import send_mail
# from django.conf import settings


def home(request):
    return render(request, "contact/contact.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.submitted_at = timezone.now()
        contact.save()
        return render(request, 'contact/contact.html', {"success": True})
    else:
        # Render the contact form
        return render(request, 'contact/contact.html')