from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.core.paginator import Paginator

# Create your views here.

class LandingPage(TemplateView):
    template_name = "landing-page/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        banners = Banner.objects.filter(page=1).values()
        about_me = AboutMe.objects.all().order_by("-id").first()
        actions = Action.objects.all().order_by("-id").first()
        item_actions = ItemAction.objects.select_related("action").filter(action__id=actions.id).values()[:3]
        project = Project.objects.all().order_by("-id").first()
        item_projects = ItemProject.objects.filter(item__id=project.id, activity=True).values()
        recruitment = Recruitment.objects.all().order_by("-id").first()
        item_recruitment = NameItemRecruitment.objects.prefetch_related(
                'name_item_recruitment'
            ).filter(item__id=recruitment.id)[:3]
        partner = Partner.objects.all().order_by("-id").first()
        item_partner = ItemPartner.objects.filter(item__id=partner.id).values()
        
        context["actions"] = actions
        context["item_actions"] = item_actions
        context['banners'] = banners
        context["about_me"] = about_me
        context["project"] = project
        context["item_projects"] = item_projects
        context["recruitment"] = recruitment
        context["item_recruitment"] = item_recruitment
        context["partner"] = partner
        context["item_partner"] = item_partner
        return context

class ProjectDetailPage(TemplateView):
    template_name = "project-detail/index.html"

class ProjectListPage(TemplateView):
    template_name = "project-list/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        projects = ItemProject.objects.all().order_by("-id").values()
        paginator = Paginator(projects, 9)

        page_number = 1
        if self.request.GET.get("page"):
            page_number = self.request.GET.get("page")

        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context
