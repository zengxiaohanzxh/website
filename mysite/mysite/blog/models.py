from django.db import models
from django.contrib.auth.models import User

from textile import textile

class Category(models.Model):
    '''
    Class for blog categories.
    '''
    
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = "categories"
        ordering = ["title"]
    
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog-categorized', kwargs={"category_slug": self.slug})
    
class Blog(models.Model):
    '''
    Class for blog posts.
    '''
    
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    lang = models.CharField(default='en', max_length=2)
    author = models.ForeignKey(User, blank=True, null=True)
    body = models.TextField(help_text="Use textile markup (http://txstyle.org/)")
    tease = models.TextField(blank=True,
                             help_text="Use textile markup (http://txstyle.org/)")
    categories = models.ManyToManyField(Category)
    pub_date = models.DateTimeField('Date Published')
    image = models.ImageField(upload_to='blog_images', blank=True)
    script = models.FilePathField(blank=True)
    allow_comments = models.BooleanField(default=False)
    highlight = models.BooleanField(default=True,
                                    help_text='Highlight this post on the front page')
    body_html = models.TextField(help_text="Valid html (not markup) for the templates", editable=False)
    tease_html = models.TextField(blank=True, editable=False)
    
    def __unicode__(self):
        return self.title

    def save(self):
        self.body_html = textile(self.body.encode('utf-8'),
                                    encoding='utf-8', output='utf-8')
        self.tease_html = textile(self.tease.encode('utf-8'),
                                    encoding='utf-8', output='utf-8')
        super(Blog, self).save()
    
    def list_categories(self):
        return ', '.join([category.title for category in self.categories.all()])
    list_categories.short_description = 'Categories'
    
    def get_absolute_url(self):
        return reverse('blog', kwargs={"slug": self.slug})
