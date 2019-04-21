from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import *



def index(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        html = (search_id)
        return HttpResponse(html)
    else:
        return render(request, 'index.html')
