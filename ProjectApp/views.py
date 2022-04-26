from django.shortcuts import render
from .forms import Projects
from .models import Projects as Pro
# Create your views here.
def insert(request , id=0):
    if request.method == "POST":
        if id > 0:
           uO =  Pro.objects.get(pk = id)
           uO.update(request.POST)
           uO.save()
           result = Pro.objects.all()
           return render(request, "ProjectApp/base1.html" ,{"result" : result})
        p =  Projects(request.POST)
        if p.is_valid:
            p.save()
        result = Pro.objects.all()
        return render(request, "ProjectApp/base1.html" ,{"result" : result})

    else:
        form = Projects()
        return render(request, "ProjectApp/base1.html" , {"form":form})

def delete(request ,id):
    pr = Pro.objects.get(pk = id)
    pr.delete()
    result = Pro.objects.all()
    return render(request, "ProjectApp/base1.html" ,{"result" : result})

def update(request ,id):
    pr = Pro.objects.get(pk = id)
    form = Projects(instance = pr)
    return render(request, "ProjectApp/base1.html" , {"form":form})

def read(request):
    result = Pro.objects.all()
    return render(request, "ProjectApp/base1.html" ,{"result" : result})
