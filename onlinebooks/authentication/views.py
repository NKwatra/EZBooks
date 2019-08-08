from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login


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
            login(request, user)
            return redirect('authenticate:sign_up')
    else:        
        form = SignUpForm()
    return render(request, 'authenticate/sign_up.html', {'form' : form})
