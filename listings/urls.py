from django.urls import path

from . import views

#route that is attached to method inside view file

urlpatterns = [
    path('', views.index, name = 'listings'), #root path
    path('<int:listing_id>', views.listing, name = 'listing'),
    path('search', views.search, name = 'search'),
]