from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import * 
from django.utils.html import mark_safe
# Register your models here.
from django.contrib.auth.models import Group

# Inline

class ItemPartnerInline(admin.TabularInline):
    model=ItemPartner
    extra=0
    
class ItemNameItemRecruitmentInlien(admin.TabularInline):
    model=ItemNameItemRecruitment
    extra=0

class ItemActionsInline(admin.TabularInline):
    model=ItemAction
    extra=0

class ItemProjectsInline(admin.TabularInline):
    model=ItemProject
    extra=0

# Admin
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ["name", "title"]
    prepopulated_fields = {"slug": ("name", "title")}

class ActionsAdmin(admin.ModelAdmin):
    list_display = ["name", "title"]

class Projectadmin(admin.ModelAdmin):
    list_display = ["name", "title"]

class NameRecruitmentAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ["name"]}
    inlines = [ItemNameItemRecruitmentInlien]

class PartnerAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [ItemPartnerInline]

class ItemProjectAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ["name"]}
    search_fields = ['name']

class RegisterAdmin(admin.ModelAdmin):
    list_display = ["full_name", "phone", "email", "status_contact", "created_at"]
    search_fields=["phone"]

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

class BannerAdmin(admin.ModelAdmin):
    list_display = ["image_tag", "page"]  # Sử dụng tên khác cho phương thức

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="/{obj.image}" width="100" height="50" />')
        return "No Image"

    image_tag.short_description = 'Image'
#   
admin.site.register(Banner, BannerAdmin)
admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Action, ActionsAdmin)
admin.site.register(Project, Projectadmin)
admin.site.register(Recruitment)
admin.site.register(NameItemRecruitment, NameRecruitmentAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(ItemProject, ItemProjectAdmin)
admin.site.register(Register, RegisterAdmin)
# 
admin.site.unregister(Group)


