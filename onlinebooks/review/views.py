from django.shortcuts import render, redirect
from django.urls import reverse
from book.models import Book
from user.models import Customer
from .models import Review

def addReview(request, book_id):
    if not (request.user.is_authenticated):
        return redirect(reverse('authenticate:authenticate'))
    customer = Customer.objects.get(user__id=request.user.id)
    book = Book.objects.get(pk=book_id)
    message=""
    if not (book in customer.orders.all()):
        head_msg="Haven't purchased this book?"
        image="/static/review/notPurchased.png"
        message = "Sorry you cannot add a review since you haven't puchased this book on EZBOOKS" 
        return render(request, "review/denyReview.html", {"Message": message, "headMessage": head_msg, "image":image}) 
    if book in customer.reviews.all():
        image="/static/review/alreadyReviewed.jpg"
        head_msg = "Already rated the book?"
        message = "Looks like you have already rated this book, you can only rate the book once"
        return render(request, "review/denyReview.html", {"Message": message, "headMessage": head_msg, "image":image}) 
    if request.method == 'GET':
        book = Book.objects.get(pk=book_id)
        return render(request, 'review/addReview.html',{'book': book}) 
    else:   
        review = request.POST["review"]
        rating = request.POST["rating"]
        current_review = Review(review=review, rating=rating, book=book, user=customer)
        current_review.save()
        return redirect(reverse('book:detail', kwargs={'book_id': book_id}))
