from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404
from datetime import date
from blog.models import Blog, Category

def homepage(request):
    current_date = date.today()
    highlighted_blogs = [blog for blog in Blog.objects.all() if blog.highlight == True]
    return render(request, 'home/home.html',
                  {'current_date':current_date,
                   'highlighted_blogs':highlighted_blogs})
