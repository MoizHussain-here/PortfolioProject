import re
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from User.models import Users,Admins
from django.contrib.auth import login , logout , authenticate


def createUser(request):
    if request.method== "POST":
        name  = request.POST['uname']
        password = request.POST['password']
        contact = "03312334664"
        email = "moiz.hussain@gmail"
        dob = "2022-03-03"
        gender = "male"
        address = "address"
        image = "image"
        isapproved = 1
        u = Users(name = name , password = password,contact=contact,email=email, dob=dob,gender=gender,address=address,image=image,is_approved=isapproved , approved_by = 1)
        u.save()
    return render(request, "base.html")

def indexUser(request):
    return render(request, "base.html")
    


def login(request):
    if request.method== "POST":
        name  = request.POST['name']
        password = request.POST['password']    
        u = authenticate(request,username = name , password = password)
        if u is not None:
            return HttpResponse(u.get_username())
    return render(request, "base.html")
   
    
def logout(request):
    pass



