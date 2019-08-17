import os
import uuid
from django import template                                                                                                              
from django.conf import settings 

register = template.Library()

@register.simple_tag(name='cache_bust')
def cache_bust():
    return '__v__={version}'.format(version=uuid.uuid1()) 
    