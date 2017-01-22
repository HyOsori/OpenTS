from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response

def search(request):
    return render_to_response('search.html')

def result(request):
    return render_to_response('result.html')