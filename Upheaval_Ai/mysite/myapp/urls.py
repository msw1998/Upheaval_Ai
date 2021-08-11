from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('3dimage', views.image, name='image'),
    path('retail-industry', views.retailindustry, name='retailindustry'),
    path('power-robotics', views.powerrobotics, name='powerrobotics'),
    path('autonomous-robots', views.autonomousrobots, name='autonomousrobots'),
    path('computer-vision', views.computervision, name='computervision'),
    path('business-intelligence', views.businessintelligence, name='businessintelligence'),
    path('defense-applications', views.defenseapplications, name='defenseapplications'),

]
