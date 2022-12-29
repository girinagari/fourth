from django.urls import path
from app2.views import *
app_name='anything'
urlpatterns = [
    path("second/",second,name='second'),
]