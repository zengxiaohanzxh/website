from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mysite.blog.models import Blog, Category

class BlogListView(ListView):
    queryset = Blog.objects.all()
    template_name = "blog/blog_index.html"
    context_object_name = 'list_blogs'
    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['list_categories'] = Category.objects.all()
        context['selected_category'] = None
        return context

class CategoryListView(BlogListView):
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['selected_category'] = self.kwargs['category_slug']
        return context

    def get_queryset(self):
        selected_category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        # Pass the chosen category blog posts to the template
        print selected_category.blog_set.all()

        return selected_category.blog_set.all()


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_content.html"
    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['list_categories'] = Category.objects.all()
        context['list_blogs'] = Blog.objects.order_by('-pub_date')
        return context
