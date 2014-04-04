from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404
from datetime import date
from mysite.blog.models import Blog, Category
from mysite.data.models import Data, DataCategory

def homepage(request):
    current_date = date.today()
    highlighted_posts = [blog for blog in Blog.objects.all() if blog.highlight == True]
    highlighted_posts += [data for data in Data.objects.all() if data.highlight == True]
    return render(request, 'home/home.html',
                  {'current_date':current_date,
                   'highlighted_blogs':highlighted_posts})
