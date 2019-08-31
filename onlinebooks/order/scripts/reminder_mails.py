from django.utils import timezone
from ..models import Order
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def run():
    rentedOrders = Order.objects.filter(order_type=1)
    for order in rentedOrders:
        if timezone.now() - order.date_of_purchase >= timezone.timedelta(days=7):
            mail_subject = "Return of book rented via EZBOOKS"
            to_email = order.user.user.email
            mail_body = render_to_string('order/returnReminder.html', { "order": order})
            email = EmailMessage(mail_subject, mail_body, to=[to_email])
            email.content_subtype = "html"
            email.send()