from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

class JobOpening(TemplateView):
    template_name = "job-opening/index.html"