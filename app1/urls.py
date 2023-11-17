from django.urls import path
from .views import *
app_name='hemanth'
urlpatterns=[
    path('data_render/',data_render,name='data_render'),
]

