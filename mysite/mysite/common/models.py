from django.db import models
from django.contrib.auth.models import User
from markdown import markdown

class Category(models.Model):
    '''
    Abstract class for post categories.
    '''
    
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    class Meta:
        ordering = ["title"]
        abstract = True
    
    def __unicode__(self):
        return self.title
    
class Post(models.Model):
    '''
    Abstract class for posts.
    '''
    
    class Meta:
        ordering = ["-pub_date"]
        abstract = True
        
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    lang = models.CharField(default='en', max_length=2)
    author = models.ForeignKey(User, blank=True, null=True)
    body = models.TextField(help_text="Use markdown")
    tease = models.TextField(blank=True,
                             help_text="Use markdown")
    allow_comments = models.BooleanField(default=False)
    highlight = models.BooleanField(default=True,
                                    help_text='Highlight this post on the front page')
    is_public = models.BooleanField(default=True,
                                    help_text='Make the post public')
    body_html = models.TextField(help_text="Valid html (not markup) for the templates", editable=False)
    tease_html = models.TextField(blank=True, editable=False)
    
    pub_date = models.DateTimeField('Date Published')
    image = models.ImageField(upload_to='blog_images', blank=True)
    show_image = models.BooleanField(default=True,
                                     help_text='Show image at the beginning of the post')
    
    def __unicode__(self):
        return self.title

    def save(self):
        self.body_html = markdown(self.body)
        self.tease_html = markdown(self.tease)
        super(Post, self).save()
