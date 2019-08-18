from django.shortcuts import render, get_object_or_404
from .models import Customer
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

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
