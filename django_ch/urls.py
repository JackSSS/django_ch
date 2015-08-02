"""django_ch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from core.views import RobotDeleteView
import core.views as coreviews


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', coreviews.LandingView.as_view()),
    url(r'robot/$', coreviews.RobotListView.as_view()),
    url(r'robot/(?P<pk>\d+)/detail/$', coreviews.DetailListView.as_view(), name='robot_list'),
    url(r'robot/create/$', coreviews.RobotCreateView.as_view()),
    url(r'search/$', coreviews.SearchListView.as_view()),
    url(r'robot/(?P<pk>\d+)/update/$', coreviews.RobotUpdateView.as_view(), name='robot_update'),
    url(r'robot/(?P<pk>\d+)/delete/$', coreviews.RobotDeleteView.as_view(), name='delete'),
]
