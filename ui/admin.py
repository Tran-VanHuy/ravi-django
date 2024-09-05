from typing import Any
from django.contrib import admin
from .models import * 
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
    inlines = [ItemActionsInline]

class Projectadmin(admin.ModelAdmin):
    list_display = ["name", "title"]
    inlines = [ItemProjectsInline]

class NameRecruitmentAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [ItemNameItemRecruitmentInlien]

class PartnerAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [ItemPartnerInline]

class ItemProjectAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ["name"]}
    search_fields = ['name']

#   
admin.site.register(Banner)
admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Action, ActionsAdmin)
admin.site.register(Project, Projectadmin)
admin.site.register(Recruitment)
admin.site.register(NameItemRecruitment, NameRecruitmentAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(ItemProject, ItemProjectAdmin)

# 
admin.site.unregister(Group)


