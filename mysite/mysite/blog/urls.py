from django.conf.urls import patterns, url
from mysite.blog.views import BlogListView, CategoryListView, BlogDetailView

POSTS_PER_PAGE = 20

urlpatterns = patterns('',
    # With class-based views we can only query the database for slugs using
    # a class method
    url(r'^$',
        BlogListView.as_view(paginate_by=POSTS_PER_PAGE),
        name="index",
        ),

    url(r'^category/(?P<category_slug>[-\w]+)$',
        CategoryListView.as_view(paginate_by=POSTS_PER_PAGE),
        name="categorized",
        ),

    url(r'^(?P<slug>[-\w]+)$',
        BlogDetailView.as_view(),
        name="content",
        ),

    url(r'^page(?P<page>[0-9]+)$',
        BlogListView.as_view(paginate_by=POSTS_PER_PAGE),
        name="paginated",
        ),
)
