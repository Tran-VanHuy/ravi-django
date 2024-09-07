from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

class JobListPage(TemplateView):
    template_name = "job-list/index.html"
