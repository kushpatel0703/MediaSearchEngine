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
        collectData(imdb_id)

    listing = Tv_details.objects.get(imdb_id=imdb_id)
    relations = list(Tv_genre.objects.filter(tv_id = listing))

    genre_list = []
    for rel in relations:
        genre_list.append(rel.genre_id.genre)

    print(genre_list)

    context = {
                'listing' : listing
            }

    return render(request, 'tvInfoPage/index.html', context)
