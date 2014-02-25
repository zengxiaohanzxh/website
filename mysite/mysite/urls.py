from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from mysite.blog.models import Blog, Category
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
#    url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mysite.home.views.homepage', name="home"),
    url(r'^blogs/', include('mysite.blog.urls', namespace="blog"))
) + \
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
