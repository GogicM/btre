from django.urls import path

from . import views

#route that is attached to method inside view file

urlpatterns = [
    path('', views.index, name = 'index'), #root path
    path('about', views.about, name = 'about'),
]