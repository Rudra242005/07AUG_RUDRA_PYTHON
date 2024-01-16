from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def index(request):
    if request.method=='POST':
        user=coustomerForm(request.POST)
        if user.is_valid():
            user.save()
            print("success")
        else:
            print(user.errors)
    return render(request,'index.html')

def clients(request):
    return render(request,'clients.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def projects(request):
    return render(request,'projects.html')

def services(request):
    return render(request,'services.html')

def estimate(request):
    return render(request,'estimate.html')