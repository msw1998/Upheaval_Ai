from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('3dimage', views.image, name='image'),
]
