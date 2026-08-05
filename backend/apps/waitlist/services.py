from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_welcome_email(email: str):
    """
    Sends the UniAGORA welcome email to a new waitlist subscriber.
    """

    subject = "🎉 Welcome to the UniAGORA Waitlist!"

    context = {
        "whatsapp_link": "https://whatsapp.com/channel/0029Vb8JuVF7oQhfrO0XoE3n",
        "linkedin_link": "https://www.linkedin.com/company/uniagorashop/about/?viewAsMember=true",
        "instagram_link": "https://www.instagram.com/uniagora.shop",
    }

    text_content = render_to_string(
        "emails/welcome.txt",
        context,
    )

    html_content = render_to_string(
        "emails/welcome.html",
        context,
    )

    message = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email],
    )

    message.attach_alternative(
        html_content,
        "text/html",
    )

    message.send()