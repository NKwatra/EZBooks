from django.shortcuts import render, get_object_or_404
from .models import Book
from review.models import Review
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
import json
from user.models import Customer

def category(request, category):
    all_books = Book.objects.filter(category__iexact=category).order_by('avg_rating').reverse()
    return render(request, 'book/category.html', {'books_list': all_books, 'category': category})

def search(request):
    query = request.GET['q']
    found_books = Book.objects.filter(Q(author__icontains=query) | Q(title__icontains=query))
    print(json.dumps(list(found_books.values())))
    return HttpResponse(json.dumps(list(found_books.values())), content_type='application/json')

def detail(request, book_id):
   book = get_object_or_404(Book, pk=book_id)
   reviews = Review.objects.filter(book__id = book_id)
   user = None
   if request.user.is_authenticated:
       user = Customer.objects.get(user__id = request.user.id)
   wishlisted = False
   if user is not None and book in user.wishlist.all():
       wishlisted = True
   return render(request, "book/detail.html", {'book': book, 'reviews': reviews, 'wishlisted': wishlisted})

def wishlist(request):
    book_id = request.GET['bookId']
    current_customer = Customer.objects.get(user__id=request.user.id)
    wishlisted_book = Book.objects.get(pk=book_id)
    if(request.GET['add'] == 'true'):
        current_customer.wishlist.add(wishlisted_book);
        return JsonResponse({'added': True})
    else:
        current_customer.wishlist.remove(wishlisted_book)
        return JsonResponse({'added': False})
