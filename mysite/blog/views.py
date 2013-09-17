from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from blog.models import Blog

def index(request):
    list_blogs = Blog.objects.order_by('-pub_date')
    context = RequestContext(request,
                             {'list_blogs':list_blogs, })
    return render(request, 'blog/blog_index.html', context)

def content(request, blog_slug):
    list_blogs = Blog.objects.order_by('-pub_date')
    blog = get_object_or_404(Blog, slug=blog_slug)
    return render(request, 'blog/blog_content.html', 
                  {'blog':blog,
                   'list_blogs':list_blogs
                   })
