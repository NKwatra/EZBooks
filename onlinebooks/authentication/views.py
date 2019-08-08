from django.shortcuts import render
from .forms import SignUpForm


def sign_up(request):
    form = SignUpForm()
    return render(request, 'authenticate/sign_up.html', {'form' : form})
