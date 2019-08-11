from django.shortcuts import render
from .models import Book
from django.db.models import Q
from django.http import HttpResponse
import json

def category(request, category):
    all_books = Book.objects.filter(category__iexact=category).order_by('avg_rating').reverse()
    return render(request, 'book/category.html', {'books_list': all_books, 'category': category})

def search(request):
    query = request.GET['q']
    found_books = Book.objects.filter(Q(author__icontains=query) | Q(title__icontains=query))
    print(json.dumps(list(found_books.values())))
    return HttpResponse(json.dumps(list(found_books.values())), content_type='application/json')
