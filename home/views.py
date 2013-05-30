# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import request

def home(request):
    """
    homepage
    """

    return render_to_response('home/home.html',
        {
            },
        context_instance = RequestContext(request))

