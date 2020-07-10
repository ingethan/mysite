from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def index(request):
    now = datetime.datetime.now()
    html = '<html><body><h2>Welcome %s<h2></body></html>' % now
    return HttpResponse(html)


def hello(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

    
