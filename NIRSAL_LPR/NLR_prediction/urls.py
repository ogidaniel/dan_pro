from django.urls import path
from . import views


#registering the urls to views in same app folder (linking)
#routing on webpage
urlpatterns =[
    path('', views.Welcome, name ='welcome'),
    
    
]