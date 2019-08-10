from django.shortcuts import render
from book.models import Book

def home(request):
    books = Book.objects.order_by('category', '-avg_rating')
    data = {}
    for book in books:
        if book.category in data:
            if len(data[book.category]) < 6 :
                data[book.category].append(book)
        else:
            data[book.category] = []
            data[book.category].append(book)               
    return render(request, 'home.html', {'data': data})