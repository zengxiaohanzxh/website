from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404
from datetime import date
from mysite.blog.models import Blog, Category
from mysite.data.models import Data, DataCategory

def homepage(request):
    current_date = date.today()
    highlighted_blogs = [blog for blog in Blog.objects.all()
                         if blog.highlight == True and blog.is_public == True]
    highlighted_data = [data for data in Data.objects.all()
                        if data.highlight == True and data.is_public == True]
    highlighted_posts = highlighted_blogs + highlighted_data
    post_urls = {}
    for post in highlighted_posts:
        if isinstance(post, Blog) == True:
            post_urls[post.slug] = 'blogs/' + post.slug
        elif isinstance(post, Data) == True:
            post_urls[post.slug] = 'data/' + post.slug
    return render(request, 'home/home.html',
                  {'current_date':current_date,
                   'highlighted_posts':highlighted_posts,
                   'post_urls':post_urls})
