from django.shortcuts import render, redirect
from django.urls import reverse
from book.models import Book
from user.models import Customer
from django.http import HttpResponse
from .models import Review

def addReview(request, book_id):
    if not (request.user.is_authenticated):
        return redirect(reverse('authenticate:authenticate'))
    if request.method == 'GET':
        book = Book.objects.get(pk=book_id)
        return render(request, 'review/addReview.html',{'book': book}) 
    else:   
        review = request.POST["review"]
        rating = request.POST["rating"]
        book = Book.objects.get(pk=book_id)
        user = Customer.objects.get(user__id = request.user.id)
        current_review = Review(review=review, rating=rating, book=book, user=user)
        current_review.save()
        return redirect(reverse('book:detail', kwargs={'book_id': book_id}))
