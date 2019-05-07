import omdb
from random import shuffle
from .models import *

def collectData(imdb_id):
    omdb.set_default('apikey', 'b5e3df7f')
    info = omdb.imdbid(imdb_id)

    print(info)

    inst = Tv_details.objects.create(
        imdb_id = imdb_id,
        title = info['title'],
        image_url = info['poster'],
        description = info['plot'],
        imdb_rating = info['imdb_rating'],
        language = info['language'],
        country = info['country'],
        year = info['year'],
        tv_rating = info['rated'])
    inst.save()

    genres = info['genre'].split(', ')
    for genre in genres:
        try:
            g = Genres.objects.get(genre=genre)
        except Genres.DoesNotExist:
            g = Genres.objects.create(genre=genre)
            g.save()

    for genre in genres:
        g = Genres.objects.get(genre=genre)
        mg = Tv_genre.objects.create(tv_id = inst, genre_id = g)
        mg.save()

def genreRetrieve(genre_list, listing):

    r = set()
    for g in genre_list:
        t = list(Tv_genre.objects.filter(genre_id = g))
        for elem in t:
            r.add(elem)

    r = list(r)

    new_r = set()
    for elem in r:
        new_r.add(Tv_details.objects.get(imdb_id = elem.tv_id.imdb_id))

    new_r = list(new_r)
    new_r.remove(listing)
    shuffle(new_r)

    return new_r
