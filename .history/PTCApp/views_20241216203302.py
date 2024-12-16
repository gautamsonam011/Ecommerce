from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home_views(request):
    # return HttpResponse("Hello")

    return JsonResponse({'Info': 'React and Django Ecomm '})