from django.conf import settings
from reports.view import views

__author__ = 'dangalg'
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload_file, name='upload_file'),
    url(r'^get_progress/$', views.get_update_progress, name='get_progress'),
    url(r'^run_algo/(?P<crashrun>0|1)/(?P<optimize>0|1)/(?P<updatedb>0|1)/(?P<algoversion>\w{1}-\d{2}-\d{2}-\d{2}-\d{2})/$', views.run_algo, name='run_algo'),
    url(r'^(?P<choice>0|1)/$', views.algovsalgo, name='algovsalgo'),
    url(r'^(?P<choice>0|1)/(?P<cycle_id1>[\d+]+)/(?P<cycle_id2>[\d+]+)/(?P<group>[\w+]+)/$', views.get_videos, name='videos'),
    url(r'^(?P<choice>0|1)/(?P<video_id>[\w+]+)/(?P<group>[\w+]+)/$', views.set_video_group, name='setvideogroup'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)