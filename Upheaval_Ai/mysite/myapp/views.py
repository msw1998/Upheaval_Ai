from django.http import HttpResponse
from django.shortcuts import render,redirect



def index(request):
    return render(request=request, 
                  template_name="myapp/index.html",)

def image(request):
    return render(request=request, 
                  template_name="myapp/new.html",)
