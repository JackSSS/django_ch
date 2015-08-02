from django.conf.urls import patterns, include, url
from django.contrib import admin
import core.views as coreviews

urlpatterns = patterns('',

 url(r'^$', coreviews.LandingView.as_view()),
 url(r'robot/$', coreviews.RobotListView.as_view()),
 url(r'robot/(?P<pk>\d+)/detail/$', coreviews.DetailListView.as_view(), name='robot_list'),
 url(r'robot/create/$', coreviews.RobotCreateView.as_view()),
 url(r'search/$', coreviews.SearchListView.as_view()),
 url(r'robot/(?P<pk>\d+)/update/$', coreviews.RobotUpdateView.as_view(), name='robot_update'),
 url(r'robot/(?P<pk>\d+)/delete/$', coreviews.RobotDeleteView.as_view(), name='delete'),
)
