from django.urls import path

from . import views

#route that is attached to method inside view file

urlpatterns = [
    path('login', views.login, name = 'login'), #function name
    path('register', views.register, name = 'register'),
    path('logout', views.logout, name = 'logout'),
    path('dashboard', views.dashboard, name = 'dashboard'),
]

#add to main urls.py