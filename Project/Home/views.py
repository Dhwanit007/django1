from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request,"index.html")

def properties(request):
    return render(request,"properties.html")

def propertydetails(request):
    return render(request,"propertydetails.html")

def contact(request):
    return render(request,"contact.html")