from django.shortcuts import render
from .models import Book

def category(request, category):
    all_books = Book.objects.filter(category__iexact=category).order_by('avg_rating').reverse()
    return render(request, 'book/category.html', {'books_list': all_books, 'category': category})