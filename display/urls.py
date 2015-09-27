from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Profile.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^home/', 'display.views.home', name='home'),
    url(r'^$', 'display.views.home'),
    # url(r'^p/P<profile_id>[0-9]+', 'display.views.profile', name='profile'),
    # url(r'^login/', 'display.views.login', name='login'),
    url(r'^profile/(?P<query>[a-zA-Z ]+)', 'display.views.profile_s', name='d_profile_s'),
    url(r'^profile/(?P<profile_id>[0-9]+)', 'display.views.profile', name='d_profile'),
    url(r'^profile', 'display.views.profile_e', name='d_profile_e'),

)
