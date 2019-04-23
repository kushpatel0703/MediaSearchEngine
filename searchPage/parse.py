import omdb

def parse_omdb(data):
    omdb.set_default('apikey', 'b5e3df7f')
    ret = omdb.search(search_id)
    print(ret)
