from django.shortcuts import render
from django.http import JsonResponse

from web.models import Data

from rest_framework.response import Response
from rest_framework.views import APIView

from web.serializers import DataSerializer

# Create your views here.
from django.shortcuts import render_to_response

def search(request):
    return render_to_response('search.html')

def result(request):
    return render_to_response('result.html')

def getshcode(request):
    return JsonResponse({
        'status': 'Success',
        'shcode': '12345'
    })

def error_response(error_code,message):
    return Response({'ErrorCode':error_code,'message':message})
def success_response(data):
    return Response({'ErrorCode':0,'message':'Success','data':data})


class Crawling(APIView):

    def get(self,format = None):
        queryset = Data.objects.all()
        if queryset != None:
            data_serializer = DataSerializer(queryset, many=True)
            return success_response(data_serializer.data)
        else:
            return error_response(-100, 'no member')

    def post(self,request,format = None):
        data_serializer = DataSerializer(data=request.data)
        if data_serializer.is_valid():
            print(1)
            data_serializer.save()
            print(data_serializer.data)
            return success_response(data_serializer.data)
        return error_response(-200, 'invalid goods')

