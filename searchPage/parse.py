import omdb

def parse_omdb(data):
    omdb.set_default('apikey', 'b5e3df7f')
    results = omdb.search(data)

    ret = []

    for result in results:
        ret.append((result['title'], result['year'], result['imdb_id'], result['poster']))

    return ret
