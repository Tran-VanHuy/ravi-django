from typing import Any
from django.views.generic import TemplateView
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404



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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['id']

        project = ItemProject.objects.filter(slug=slug).first()
        project_other = ItemProject.objects.exclude(id=project.id).all().order_by("-id")[:3]
        
        context["project"] = project
        context["project_other"] = project_other
        return context

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

def RegisterVoucher(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            full_name = request.POST.get("fullName")
            phone = request.POST.get("phone")
            email = request.POST.get("email")

            register = Register(full_name=full_name, phone=phone, email=email, status_contact=False)
            register.save()

            context = {
                "message": "SUCCESS",
                "status": 200,
                "data": None
            }

            return JsonResponse({"context": context})

    return HttpResponseBadRequest('Invalid request')

class JobListPage(TemplateView):
    template_name = "job-list/index.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        recruitment = Recruitment.objects.all().order_by("-id").first()
        item_recruitment = NameItemRecruitment.objects.prefetch_related(
            Prefetch("name_item_recruitment",
            queryset = ItemNameItemRecruitment.objects.filter(show_job_list=True))
        ).all().order_by("-id")

        pageSize = 6

        if self.request.GET.get("page_size") and pageSize > 6:
            pageSize = self.request.GET.get("page_size")

        paginator = Paginator(item_recruitment, pageSize)
        page_obj = paginator.get_page(1)

        data_last = paginator.count - len(page_obj.object_list)
        page_size_last = len(page_obj.object_list) + data_last

        context["recruitment"] = recruitment 
        context["item_recruitment"] = page_obj
        context["data_last"] = data_last
        context["page_size_last"] = page_size_last
        return context
    

class JobOpening(TemplateView):
    template_name = "job-opening/index.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['id']

        recruitment = NameItemRecruitment.objects.prefetch_related(
            "name_item_recruitment"
        ).filter(slug=slug).first()
        area = Area.objects.all().order_by("-id")

        context["recruitment"] = recruitment
        context["area"] = area
        return context

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        full_name = request.POST.get("full_name")
        date_of_birth = request.POST.get("date_of_birth")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        area = request.POST.get("area")
        resume_cv = request.FILES.get("file_cv")
        application_letter = request.POST.get("application_letter")
        recruitment_id = request.POST.get("recruitment")

        recruitment = get_object_or_404(NameItemRecruitment, pk=recruitment_id)

        apply = Apply(full_name=full_name, date_of_birth=date_of_birth, phone=phone, email=email, area=area, resume_cv=resume_cv, application_letter=application_letter, recruitment=recruitment)
        apply.save()

        if apply:
            context["message"]="Ứng tuyển thành công...!"
        
        context["recruitment"] = recruitment
        return self.render_to_response(context)
    
