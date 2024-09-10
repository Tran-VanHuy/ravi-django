from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class LandingPage(TemplateView):
    template_name = "landing-page/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context

class ProjectDetailPage(TemplateView):
    template_name = "project-detail/index.html"

class ProjectListPage(TemplateView):
    template_name = "project-list/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AboutPage(TemplateView):
    template_name="about/index.html"

class JobListPage(TemplateView):
    template_name = "job-list/index.html"
    
class JobOpening(TemplateView):
    template_name = "job-opening/index.html"

def error_404(request, exception):
    print("vào đay 2")
    return render(request, '404.html', status=404)
