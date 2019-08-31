from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from order.models import Order
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        rentedOrders = Order.objects.filter(order_type=1)
        for order in rentedOrders:
            if timezone.now() - order.date_of_purchase >= timezone.timedelta(days=7):
                mail_subject = "Return of book rented via EZBOOKS"
                to_email = order.user.user.email
                mail_body = render_to_string('order/returnReminder.html', { "order": order})
                email = EmailMessage(mail_subject, mail_body, to=[to_email])
                email.content_subtype = "html"
                email.send()