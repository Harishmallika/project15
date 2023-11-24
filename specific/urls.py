from specific.views import *
from django.urls import path

app_name='specific'


urlpatterns=[
    path('anil/',anil,name='anil'),
    path('venke/',venke,name='venke'),
]