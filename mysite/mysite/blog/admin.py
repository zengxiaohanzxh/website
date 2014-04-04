from django.contrib import admin
from mysite.blog.models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    '''
    Class for Blog administration.
    '''
    list_display = ['title', 'list_categories', 'pub_date', 'highlight', 'is_public']
    list_filter = ['pub_date', 'categories', 'highlight', 'is_public']
    search_field = ['title', 'categories']
    date_hierarchy = 'pub_date'
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
