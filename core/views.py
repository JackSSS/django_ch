from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from core.models import Robot
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

class RobotCreateView(CreateView):
    model = coremodels.Robot
    template_name = 'base/form.html'
    fields = "__all__"

class RobotUpdateView(UpdateView):
    model = coremodels.Robot
    template_name = 'base/form.html'
    fields = "__all__"

class RobotDeleteView(DeleteView):
    model = coremodels.Robot
    template_name = 'robot/delete.html'
    context_object_name = 'item'
    success_url = reverse_lazy('list')

class SearchListView(RobotListView):
    def get_queryset(self):
        incoming_query_string = self.request.GET.get('query', '')
        return coremodels.Robot.objects.filter(name__icontains=incoming_query_string)
