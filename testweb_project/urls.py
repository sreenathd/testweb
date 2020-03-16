from django.conf.urls import url
from django.contrib import admin, admindocs
#from testweb_app import views
from testweb_app import views as myapp_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', myapp_views.UserViewSet)
router.register(r'groups', myapp_views.GroupViewSet)

'''
urlpatterns = [
    url(r'^$', myapp_views.main, name='home'),
    url(r'^stress/$', myapp_views.stress_test, name='contact'),
    url(r'^login/$', myapp_views.login_user, name='login'),
    url(r'^admin/doc/', admindocs.urls),
    url(r'^admin/', admin.site.urls),
]
'''

urlpatterns = [
    # Examples:
    # url(r'^$', 'testweb_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^main/$', myapp_views.main),
    url(r'^$', myapp_views.main, name="main"),
    url(r'^login/$', myapp_views.login_user),
    url(r'^logout/$', myapp_views.logout_user),
    url(r'^stress/$', myapp_views.stress_test),
    #url(r'^admin/doc/', admindocs.urls),
    url(r'^admin/', admin.site.urls),
    #path('', router.urls),
    #path('api-auth/', 'rest_framework.urls', namespace='rest_framework'),
    
]

