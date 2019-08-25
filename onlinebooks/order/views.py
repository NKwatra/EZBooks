from django.shortcuts import render, redirect,reverse
from django.contrib.auth.decorators import login_required
from book.models import Book
from user.models import Customer
from .models import Order

@login_required(login_url='authenticate:authenticate')
def newOrder(request, book_id, order_type):
    book = Book.objects.get(pk=book_id)
    customer = Customer.objects.get(user__id = request.user.id)
    return render(request, 'order/orderSummary.html', {'book': book, 'user': customer, 'type': order_type})

@login_required(login_url='authenticate:authenticate')
def placeOrder(request, book_id, type):
    book = Book.objects.get(pk=book_id)
    customer = Customer.objects.get(user__id=request.user.id)
    Order.objects.create(book=book, user=customer, order_type=type)  
    return redirect(reverse('user:myOrders', kwargs={"user_id": customer.user.id})) 
