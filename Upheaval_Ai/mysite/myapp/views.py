from django.http import HttpResponse
from django.shortcuts import render,redirect



def index(request):
    return render(request=request, 
                  template_name="myapp/index.html",)

def image(request):
    return render(request=request, 
                  template_name="myapp/new.html",)
def retailindustry(request):
    return render(request=request, 
                  template_name="myapp/retail-industry.html",)

def powerrobotics(request):
    return render(request=request, 
                  template_name="myapp/power-robotics.html",)

def autonomousrobots(request):
    return render(request=request, 
                  template_name="myapp/autonomous-robots.html",)

def computervision(request):
    return render(request=request, 
                  template_name="myapp/computer-vision.html",)

def businessintelligence(request):
    return render(request=request, 
                  template_name="myapp/business-intelligence.html",)

def defenseapplications(request):
    return render(request=request, 
                  template_name="myapp/defense-applications.html",)
