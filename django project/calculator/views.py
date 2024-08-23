import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add(request):
    data = json.loads(request.body)
    num = data.get('numbers')
    total=sum(num)
    return JsonResponse({"Sum":total})
    

@csrf_exempt
def avg(request):
    data = json.loads(request.body)
    num = data.get('numbers')
    total=sum(num)
    length=len(num)
    return JsonResponse ({"avg":total/length})

@csrf_exempt
def product(request):
    data = json.loads(request.body)
    num = data.get('numbers')
    prod=1
    for i in num:
        prod*=i
    return JsonResponse ({"product":prod})