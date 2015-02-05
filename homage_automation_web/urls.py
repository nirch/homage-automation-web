from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homage_automation_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


url(
    regex=r'^login/$',
    view=login,
    kwargs={'template_name': 'login.html'},
    name='login'
),
url(
    regex=r'^logout/$',
    view=logout,
    kwargs={'next_page': '/login'},
    name='logout'
),
    # url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reports/', include('reports.view.urls')),
)
