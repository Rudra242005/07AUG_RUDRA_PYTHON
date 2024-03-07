from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def index(request):
    if request.method=="POST":
        products = productForm(request.POST)
        if products.is_valid():
            products.save()
            print('your data has been saved successfully!')
        else:
            print('error')
    return render(request,'index.html')

def showdata(request):
    return render(request,'showdata.html')