from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mysite.data.models import Data, DataCategory

class DataListView(ListView):
    queryset = Data.objects.all()
    template_name = "data/data_index.html"
    context_object_name = 'list_datas'
    def get_context_data(self, **kwargs):
        context = super(DataListView, self).get_context_data(**kwargs)
        context['list_categories'] = DataCategory.objects.all()
        context['selected_category'] = None
        return context

class DataCategoryListView(DataListView):
    def get_context_data(self, **kwargs):
        context = super(DataCategoryListView, self).get_context_data(**kwargs)
        context['selected_category'] = self.kwargs['category_slug']
        return context

    def get_queryset(self):
        selected_category = get_object_or_404(DataCategory, slug=self.kwargs['category_slug'])
        return selected_category.data_set.all()


class DataDetailView(DetailView):
    model = Data
    template_name = "data/data_content.html"
    context_object_name = 'data'
    def get_context_data(self, **kwargs):
        context = super(DataDetailView, self).get_context_data(**kwargs)
        context['list_categories'] = DataCategory.objects.all()
        context['list_datas'] = Data.objects.order_by('-pub_date')
        return context
