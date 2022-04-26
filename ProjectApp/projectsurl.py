
from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.read),
    path('insert', views.insert),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
]
