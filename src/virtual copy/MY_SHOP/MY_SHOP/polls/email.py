from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.cache import cache


#_______________________________________________________________________________


def send_verification_email(user):
    # Generate a random verification code
    verification_code = get_random_string(length=32)

    # Cache the verification code using the user's email as the key
    cache.set(user.email, verification_code)

    # Render the verification email template with the verification code
    context = {'verification_code': verification_code}
    html_message = render_to_string('verification_email.html', context)
    plain_message = strip_tags(html_message)

    # Send the email using Django's built-in email sending functionality
    subject = 'Verify your email'
    from_email = settings.EMAIL_FROM_ADDRESS
    recipient_list = [user.email]
    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
