from django.contrib import admin
from .models import Realtor


#to display additional fields in List in Admin panel
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    #to make field clickable - linked
    list_display_links = ('id', 'name')
    #for adding filter
   # list_filter = ('realtor',)
    #publish unpublish 
    #list_editable = ('is_published',)
    #search by fields
    search_fields = ('name', )
    #pagination
    list_per_page = 25

#Register models to admin area
admin.site.register(Realtor, RealtorAdmin)

#admin.site.register(Realtor)
