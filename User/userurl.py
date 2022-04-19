import imp
from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    
    path('', views.indexUser),
    path('login', views.login),
    path('logout', views.logout),
    path('signup', views.createUser),
]
