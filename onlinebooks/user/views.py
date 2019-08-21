from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

@login_required(login_url='authenticate:authenticate')
@ensure_csrf_cookie
def profile(request, user_id):
    customer = get_object_or_404(Customer, user__id=user_id)
    return render(request, 'user/profile.html', {'customer': customer})

def ajaxUpdate(request, user_id):
    customer = get_object_or_404(Customer, user__id = user_id)
    key = request.POST.getlist('attribute[]')
    if key[0] == 'address':
        customer.address = key[1]
    elif key[0] == 'mobile_no':
        customer.mobile_no = key[1]          
    customer.save()
    return JsonResponse({'key': key[0].capitalize().replace("_", " ")})  

@login_required(login_url='authenticate:authenticate')
def password_change(request):    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect(reverse("user:profile", kwargs={'user_id': request.user.id}))
        else:
            pass 
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "user/password_change.html", {'form': form})                   
