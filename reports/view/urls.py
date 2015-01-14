from reports.view import views

__author__ = 'dangalg'
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<choice>0|1)/$', views.algovsalgo, name='algovsalgo'),
    url(r'^(?P<choice>0|1)/(?P<cycle_id1>[\d+]+)/(?P<cycle_id2>[\d+]+)/(?P<group>[\w+]+)/$', views.get_videos, name='videos'),
    url(r'^(?P<choice>0|1)/(?P<video_id>[\w+]+)/(?P<group>[\w+]+)/$', views.set_video_group, name='setvideogroup'),
)