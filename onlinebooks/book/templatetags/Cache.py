import os
import uuid
import datetime
from django import template                                                                                                              
from django.conf import settings 

register = template.Library()

@register.simple_tag(name='cache_bust')
def cache_bust():
    return '__v__={version}'.format(version=uuid.uuid1()) 

@register.filter
def plus_days(value, days):
    return value + datetime.timedelta(days=days)   

@register.filter
def divide(value,divisor):
    return value // divisor   