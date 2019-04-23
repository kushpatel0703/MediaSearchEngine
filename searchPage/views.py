from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import *
from searchPage.parse import parse_omdb


def index(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        ret = parse(search_id)

        html = (to_display)
        return HttpResponse(html)
    else:
        return render(request, 'index.html')
