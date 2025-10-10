from django.shortcuts import render
from rest_framework.decorators  import api_view
from rest_framework.response import Response
from django.http import HttpResponse



@api_view(['GET'])
def hello_world (request):
    return  Response({ 'message' : "Hello, world! This is your first DRF API!"})


def greet_user( request):
    name = request.GET.get('name', 'Guest')
    message = f'Hello {name} Welcome to Python and Django!'
    return HttpResponse(message)
