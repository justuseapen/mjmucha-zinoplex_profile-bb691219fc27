from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Profile.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^autocomplete/(?P<query>[\w\s]+)', 'api.views.autocomplete', name='autocomplete')
)
