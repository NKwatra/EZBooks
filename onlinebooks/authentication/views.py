from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login as sign_in, logout as sign_out
from django.urls import reverse
from django.contrib.auth.forms import SetPasswordForm
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from user.models import Customer
from django.contrib.auth.models import User
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import re

def auth(request):
    form = SignUpForm()
    next = request.GET.get("next")
    return render(request, 'authenticate/auth.html', {'form': form, "next": next})

def sign_up(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.username = user.email
        user.is_active = False;
        user.save()
        user.refresh_from_db()
        user.customer.address = form.cleaned_data.get('address')
        mobile = form.cleaned_data.get('mobile_no').replace(' ', '')
        if re.search("^[+]", mobile):
            user.customer.mobile_no = mobile
        else:    
            user.customer.mobile_no = "+" + mobile
        user.save()
        mail_subject = 'Activation of account for EZBOOKS'
        mail_body = render_to_string('authenticate/emailVerification.html',{
            'user': user,
            'domain': get_current_site(request).domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(mail_subject, mail_body, to=[to_email])
        email.content_subtype = "html"
        email.send()
        return render(request, 'authenticate/emailConfirmation.html',{'email': user.email})
    else:    
        return render(request, 'authenticate/auth.html', {'form': form, 'active_tab': 'signup'})   

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=email, password=password)
    next = request.GET.get("next")
    if user is not None:
        sign_in(request, user)
        return redirect(next)
    else :
        error_message = 'Incorrect username or password'
        return render(request, 'authenticate/auth.html', {'error': error_message, 'form': SignUpForm(),
         'active_tab': 'login', "next": next })

def logout(request):
    sign_out(request)
    return redirect(reverse('home'))

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64)) 
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, User.DoesNotExist, OverflowError):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        sign_in(request, user)
        return redirect(reverse('home'))
    else:
        return HttpResponse("This link is no longer valid, please sign up again")    

def checkEmail(request):
    email_id = request.GET.get("email")
    try:
        user = User.objects.get(email__iexact=email_id)
        return JsonResponse({"exists": True})
    except User.DoesNotExist:
        return JsonResponse({"exists": False})

def password_reset(request):
    if request.method == "GET":
        return render(request, "authenticate/password_reset.html")
    else:
        email = request.POST.get("email")
        print(email)
        customer = Customer.objects.get(user__email__iexact=email)
        user = customer.user
        mail_subject = "Password reset for EZBOOKS account"
        mail_body = render_to_string('authenticate/passwordResetMail.html', {
            "user": user,
            'domain': get_current_site(request).domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = email
        sentEmail = EmailMessage(mail_subject, mail_body, to=[to_email])
        sentEmail.content_subtype = 'html'
        sentEmail.send()
        return render(request, "authenticate/passwordResetDone.html")

def password_change(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64)) 
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, User.DoesNotExist, OverflowError):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        if request.method == "POST":
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return render(request, "authenticate/passwordDone.html")
            else:
                return render(request, "authenticate/passwordChange.html", {
                "form": form,
                "uidb64": uidb64,
                "token": token
                })  
        else: 
            return render(request, "authenticate/passwordChange.html", {
        "form": SetPasswordForm(user),
        "uidb64": uidb64,
        "token": token
        })           