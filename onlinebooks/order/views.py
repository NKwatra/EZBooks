from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from book.models import Book
from user.models import Customer

@login_required(login_url='authenticate:authenticate')
def newOrder(request, book_id, order_type):
    book = Book.objects.get(pk=book_id)
    customer = Customer.objects.get(user__id = request.user.id)
    return render(request, 'order/orderSummary.html', {'book': book, 'user': customer, 'type': order_type})

@login_required(login_url='authenticate:authenticate')
def placeOrder(request, book_id, type):
    pass    
