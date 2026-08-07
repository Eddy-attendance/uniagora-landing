import requests

from django.conf import settings
from django.template.loader import render_to_string


BREVO_API_URL = "https://api.brevo.com/v3/smtp/email"


def send_welcome_email(email: str):
    """
    Sends the UniAGORA welcome email using Brevo's Transactional Email API.
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

    payload = {
        "sender": {
            "name": "UniAGORA",
            "email": "eddyolly23@gmail.com",
        },
        "to": [
            {
                "email": email,
            }
        ],
        "subject": subject,
        "textContent": text_content,
        "htmlContent": html_content,
    }

    headers = {
        "accept": "application/json",
        "api-key": settings.BREVO_API_KEY,
        "content-type": "application/json",
    }

    response = requests.post(
        BREVO_API_URL,
        json=payload,
        headers=headers,
        timeout=15,
    )

    response.raise_for_status()

    print(f"✅ Brevo email sent to {email}")

    return response.json()