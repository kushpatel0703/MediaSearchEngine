from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the TV Info Page index.")

def details(request, imdb_id):
    return HttpResponse("You're looking at id %s." % imdb_id)
