from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login as sign_in, logout as sign_out
from django.urls import reverse

def auth(request):
    form = SignUpForm()
    return render(request, 'authenticate/auth.html', {'form': form})

def sign_up(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.username = user.email
        user.save()
        user.refresh_from_db()
        user.customer.address = form.cleaned_data.get('address')
        user.customer.mobile_no = form.cleaned_data.get('mobile_no').replace(' ', '')
        user.save()
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=user.email, password=raw_password)
        sign_in(request, user)
        return redirect(reverse('authenticate:authenticate'))
    return render(request, 'authenticate/auth.html', {'form': form, 'active_tab': 'sign-up'})   

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=email, password=password)
    if user is not None:
        sign_in(request, user)
        return redirect(reverse('authenticate:authenticate'))
    else :
        error_message = 'Incorrect username or password'
        return render(request, 'authenticate/auth.html', {'error': error_message, 'form': SignUpForm(),
         'active_tab': 'login' })

def logout(request):
    sign_out(request)
    return redirect(reverse('authenticate:authenticate'))