from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import core.models as coremodels

# Create your views here.

class LandingView(TemplateView):
    template_name = 'base/index.html'

class RobotListView(ListView):
    model = coremodels.Robot
    template_name = 'robot/list.html'

class DetailListView(DetailView):
    model = coremodels.Robot
    template_name = 'robot/detail.html'
    context_object_name = 'robot'
