from django.contrib import admin
from blog.models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    '''
    Class for Blog administration.
    '''
    list_display = ['title', 'list_categories', 'pub_date', 'highlight']
    list_filter = ['pub_date', 'categories']
    search_field = ['title', 'categories']
    date_hierarchy = 'pub_date'
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
