from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Profile.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^', include('django.contrib.auth.urls')),
    url(r'^lgo/', 'django.contrib.auth.views.logout_then_login', name='d_logout'),
    url(r'^', include('display.urls')),
    url(r'^display/', include('display.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),


)
