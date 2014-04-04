from django.db import models
from mysite.common.models import Post, Category

class DataCategory(Category):
    '''
    Class for data categories.
    '''
    
    class Meta:
        verbose_name_plural = "data categories"
    
    def get_absolute_url(self):
        return reverse('data-categorized', kwargs={"category_slug": self.slug})
    
class Data(Post):
    '''
    Class for Data posts.
    '''
    
    categories = models.ManyToManyField(DataCategory)
    code = models.TextField(help_text="Add code here", blank=True)
    
    def list_categories(self):
        return ', '.join([category.title for category in self.categories.all()])
    list_categories.short_description = 'Categories'
    
    def get_absolute_url(self):
        return reverse('blog', kwargs={"slug": self.slug})
