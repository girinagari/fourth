from django.urls import path
from app1.views import *
app_name='sommething'

urlpatterns = [
    path("first/",first,name="first"),
]