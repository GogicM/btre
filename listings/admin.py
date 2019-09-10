from django.contrib import admin

from .models import Listing

#to display additional fields in List in Admin panel
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    #to make field clickable - linked
    list_display_links = ('id', 'title')
    #for adding filter
    list_filter = ('realtor',)
    #publish unpublish 
    list_editable = ('is_published',)
    #search by fields
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    #pagination
    list_per_page = 25

#Register models to admin area
admin.site.register(Listing, ListingAdmin)
