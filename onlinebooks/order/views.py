from django.shortcuts import render, redirect,reverse
from django.contrib.auth.decorators import login_required
from book.models import Book
from user.models import Customer
from .models import Order
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage

@login_required(login_url='authenticate:authenticate')
def newOrder(request, book_id, order_type):
    book = Book.objects.get(pk=book_id)
    customer = Customer.objects.get(user__id = request.user.id)
    return render(request, 'order/orderSummary.html', {'book': book, 'user': customer, 'type': order_type})

@login_required(login_url='authenticate:authenticate')
def placeOrder(request, book_id, type):
    book = Book.objects.get(pk=book_id)
    customer = Customer.objects.get(user__id=request.user.id)
    current_order = Order.objects.create(book=book, user=customer, order_type=type) 
    mail_subject = "Order Confirmation- Your order with EZBOOKS has been successfully placed"
    to_email = customer.user.email
    mail_body = render_to_string('order/confirmation.html', {
        "book": book,
        "customer": customer,
        "order": current_order,
        'domain': get_current_site(request).domain,
    })
    email = EmailMessage(mail_subject, mail_body, to=[to_email])
    email.content_subtype = "html"
    email.send()
    return redirect(reverse('user:myOrders', kwargs={"user_id": customer.user.id})) 
