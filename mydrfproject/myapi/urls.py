from django.urls import path
from myapi.views import *

urlpatterns = [
    
    path('test/', hello_world , name='test'),
    path('greet/', greet_user, name='greet_user'),
]
