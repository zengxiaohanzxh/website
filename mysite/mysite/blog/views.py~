from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Blog, Category

def index(request):
    list_categories = Category.objects.all()
    years = []
    
    blogs = Blog.objects.order_by('-pub_date')
    paginator = Paginator(blogs, 25)
    page = request.GET.get('page')
    try:
        list_blogs = paginator.page(page)
    except PageNotAnInteger:
        list_blogs = paginator.page(1)
    except EmptyPage:
        list_blogs = paginator.page(paginator.num_pages)
           
    context = RequestContext(request,
                             {'list_blogs':list_blogs,
                              'list_categories':list_categories})
    return render(request, 'blog/blog_index.html', context)

def content(request, blog_slug):
    list_blogs = Blog.objects.order_by('-pub_date')
    blog = get_object_or_404(Blog, slug=blog_slug)
    return render(request, 'blog/blog_content.html',
                  {'blog':blog,
                   'list_blogs':list_blogs
                   })
