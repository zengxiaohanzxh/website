from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Blog

def index(request):
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
                             {'list_blogs':list_blogs, })
    return render(request, 'blog/blog_index.html', context)

def content(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    return render(request, 'blog/blog_content.html',
                  {'blog':blog,
                   })
