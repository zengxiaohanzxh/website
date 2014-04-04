from django.contrib import admin
from mysite.data.models import Data, DataCategory

class DataAdmin(admin.ModelAdmin):
    '''
    Class for Dada administration.
    '''
    list_display = ['title', 'list_categories', 'pub_date', 'highlight', 'is_public']
    list_filter = ['pub_date', 'categories', 'highlight', 'is_public']
    search_field = ['title', 'categories']
    date_hierarchy = 'pub_date'
    
admin.site.register(Data, DataAdmin)
admin.site.register(DataCategory)
