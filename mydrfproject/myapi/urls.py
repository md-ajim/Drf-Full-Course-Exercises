from django.urls import path
from myapi.views import *

urlpatterns = [
    
    path('test/', hello_world , name='test')
]
