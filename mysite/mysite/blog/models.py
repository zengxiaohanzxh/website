from django.db import models
from mysite.common.models import CommonPost, CommonCategory

class Category(CommonCategory):
    '''
    Class for blog categories.
    '''
    
    class Meta:
        verbose_name_plural = "blog categories"
    
    def get_absolute_url(self):
        return reverse('blog-categorized', kwargs={"category_slug": self.slug})
    
class Blog(CommonPost):
    '''
    Class for blog posts.
    '''
    
    categories = models.ManyToManyField(Category)
    script = models.TextField(help_text="Add scripts here", blank=True)
    
    def list_categories(self):
        return ', '.join([category.title for category in self.categories.all()])
    list_categories.short_description = 'Categories'
    
    def get_absolute_url(self):
        return reverse('blog', kwargs={"slug": self.slug})
