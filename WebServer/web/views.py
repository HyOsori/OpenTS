from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

from django.shortcuts import render_to_response

def search(request):
    return render_to_response('search.html')

def result(request):
    return render_to_response('result.html')

def getshcode(request):
    keyword = request.GET['keyword']

    if keyword == 'SAMSUNG':
        return JsonResponse({
            'status': 'OK',
            'shcode': 1000
        })
    else:
        return JsonResponse({
            'status': 'Failure',
            'shcode': -1
        })

def crawl(request):
    return JsonResponse({})