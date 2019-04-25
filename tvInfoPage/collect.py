import omdb
from .models import *

def collectData(imdb_id):
    omdb.set_default('apikey', 'b5e3df7f')
    info = omdb.imdbid(imdb_id)

    print(info)

    inst = Tv_details.objects.create(imdb_id = imdb_id, title = info['title'], image_url = info['poster'], description = info['plot'], imdb_rating = info['imdb_rating'])
    #inst.save()

    genres = info['genre'].split(', ')
    print(genres)



    return 0
