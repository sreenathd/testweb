from django.conf.urls import patterns, include, url
from django.contrib import admin
from turnkey_app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'turnkey_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^main/$', views.main),
    url(r'^$', views.main, name="main"),
    url(r'^login/$', views.login_user),
    url(r'^logout/$', views.logout_user),
    url(r'^stress/$', views.stress_test),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)
