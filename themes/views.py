from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class CompanyDetailView(TemplateView):
    template_name = 'themes/company-detail.html'


class CompanyPeopleView(TemplateView):
    template_name = 'themes/company-people.html'


class CompanySettingView(TemplateView):
    template_name = 'themes/company-settings.html'


class CompanyTaskDetailView(TemplateView):
    template_name = 'themes/company-task-detail.html'


class CompanyTaskView(TemplateView):
    template_name = 'themes/company-task.html'
