from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login as sign_in, logout as sign_out


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.customer.address = form.cleaned_data.get('address')
            user.customer.mobile_no = form.cleaned_data.get('mobile_no').replace(' ', '')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            sign_in(request, user)
            return redirect('authenticate:sign_up')
    else:        
        form = SignUpForm()
    return render(request, 'authenticate/sign_up.html', {'form' : form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            sign_in(request, user)
            return redirect('authenticate:login')
        else :
            error_message = 'Incorrect username or password'
            return render(request, 'authenticate/login.html', {'error': error_message })
    return render(request, 'authenticate/login.html') 

def logout(request):
    sign_out(request)
    return redirect('authenticate:login')