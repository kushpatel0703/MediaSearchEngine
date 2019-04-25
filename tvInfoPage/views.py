from django.shortcuts import render
from django.http import HttpResponse
from tvInfoPage.collect import collectData

from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the TV Info Page index.")

def details(request, imdb_id):
    try:
        listing = Tv_details.objects.get(imdb_id=imdb_id)
    except Tv_details.DoesNotExist:
        ret = collectData(imdb_id)
        return HttpResponse("None")
    return HttpResponse("You're looking at id %s." % imdb_id)
