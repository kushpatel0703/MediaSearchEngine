from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import *
from searchPage.parse import parse_omdb


def index(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        data = parse_omdb(search_id)

        context = {
            'data' : data
        }
        
        return render(request, 'searchPage/results.html', context)
    else:
        return render(request, 'searchPage/index.html')
