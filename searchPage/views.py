from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import *
import omdb

def index(request):
    omdb.set_default('apikey', 'b5e3df7f')
    if request.method == 'POST':
        to_display = []

        search_id = request.POST.get('textfield', None)
        ret = omdb.search(search_id)

        for elem in ret:
            to_display.append(elem)

        html = (to_display)
        return HttpResponse(html)
    else:
        return render(request, 'index.html')
