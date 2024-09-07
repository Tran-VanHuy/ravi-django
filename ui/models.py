from typing import Any
from django.db import models
from .enums import *
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Banner(models.Model):
    image = models.ImageField(upload_to="static/images", unique=True, blank=True, null=True)
    page = models.IntegerField(
        choices=[
            (PageEnums.HOME_PAGE.value, "HOME_PAGE"),
            (PageEnums.PROJECT.value, "PROJECT")
        ],
        verbose_name="Page"
    )

    def __str__(self) -> str:
        return f"{self.page}"
    
    class Meta:
        db_table="banners"
        verbose_name="banners"
        verbose_name_plural="banners"

class AboutMe(models.Model):
    image = models.ImageField(upload_to="static/images", unique=True, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    desc = models.TextField(verbose_name="Short desc")
    content = RichTextUploadingField(verbose_name="Content")
    slug = models.SlugField(default="", null=False)

    def __str__(self) -> str:
        return f'{self.name} - {self.title}'
    
    class Meta:
        db_table="abouts"
        verbose_name="Về chúng tôi"
        verbose_name_plural="Về chúng tôi"

class Action(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        db_table="actions"
        verbose_name="Hoạt động"
        verbose_name_plural="Hoạt động"

class ItemAction(models.Model):
    icon = models.TextField(verbose_name="Icon")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    desc = models.TextField(verbose_name="Short desc")
    content =  RichTextUploadingField(verbose_name="Content")
    slug = models.SlugField()
    action = models.ForeignKey(
        Action,
        related_name="action",
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        db_table="item_actions"
        verbose_name="Hoạt động (Item)"
        verbose_name_plural="Hoạt động (Item)"

class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name="name")
    title = models.CharField(max_length=255, verbose_name="title")

    class Meta:
        db_table="projects"
        verbose_name="Dự án"
        verbose_name_plural="Dự án"
    
    def __str__(self):
        return f'{self.name}'


class ItemProject(models.Model):
    image = models.FileField(upload_to="static/images", unique=True, verbose_name="image")
    name = models.CharField(max_length=255, verbose_name="name")
    address = models.CharField(max_length=255, verbose_name="address")
    content = RichTextUploadingField()
    activity = models.BooleanField(verbose_name="activity", default=True)
    item = models.ForeignKey(
        Project,
        related_name="project",
        blank=True,
        null=True,
        verbose_name="item",
        on_delete=models.CASCADE
    )
    slug = models.SlugField(default="", null=False)

    class Meta:
        db_table="item_projects"
        verbose_name="Dự án (Item)"
        verbose_name_plural="Dự án (Item)"
    
    def __str__(self) -> str:
        return f'{self.name}'
    
class Recruitment(models.Model):
    name = models.CharField(max_length=255, verbose_name="name")
    title = models.TextField(verbose_name="title")
    image = image = models.FileField(upload_to="static/images", unique=True, verbose_name="image")

    class Meta:
        db_table="recruitment"
        verbose_name="Tuyển dụng"
        verbose_name_plural="Tuyển dụng"
    
    def __str__(self) -> str:
        return f'{self.name}'

class NameItemRecruitment(models.Model):
    name = models.CharField(max_length=255, verbose_name="name")
    work = models.CharField(
        max_length=255,
        choices=[
            (WorkEnums.FULL_TIME.value, "FULL TIME"),
            (WorkEnums.PART_TIME.value, "PART TIME")
        ],
        verbose_name="work",
        blank=True,
        null=True
    )
    content = RichTextUploadingField(verbose_name="content", blank=True, null=True)
    item = models.ForeignKey(
        Recruitment,
        null=True,
        verbose_name="item",
        related_name="recruitment",
        on_delete=models.CASCADE
    )

    class Meta:
        db_table="name_item_recruitment"
        verbose_name="Tuyển dụng (Item)"
        verbose_name_plural="Tuyển dụng (Item)"
    
    def __str__(self) -> str:
        return f'{self.name}'

class ItemNameItemRecruitment(models.Model):
    name = models.CharField(max_length=255, verbose_name="name")
    content = models.CharField(max_length=255, verbose_name="content")
    item = models.ForeignKey(
        NameItemRecruitment,
        blank=True,
        null=True,
        verbose_name="item",
        related_name="name_item_recruitment",
        on_delete=models.CASCADE
    )

    class Meta:
        db_table="item_name_item_recruitment"
        verbose_name="Tuyển dụng (Item in item)"
        verbose_name_plural="Tuyển dụng (Item in item)"
    
    def __str__(self) -> str:
        return f'{self.name}'

class Partner(models.Model):
    name = models.CharField(max_length=255, verbose_name="name")
    desc = models.TextField(verbose_name="description")

    class Meta:
        db_table="partners"
        verbose_name="Đối tác"
        verbose_name_plural="Đối tác"
    
    def __str__(self) -> str:
        return f'{self.name}'


class ItemPartner(models.Model):
    image = models.FileField(upload_to="static/images", unique=True, verbose_name="image")
    link = models.TextField(verbose_name="link")
    item = models.ForeignKey(
        Partner,
        blank=True,
        null=True,
        verbose_name="item",
        related_name="item_partner",
        on_delete=models.CASCADE
    )
    class Meta:
        db_table="item_partners"
        verbose_name="Đối tác (item)"
        verbose_name_plural="Đối tác (item)"
    
    def __str__(self) -> str:
        return f'{self.link}'

class Register(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Full name")
    phone = models.CharField(max_length=255, verbose_name="Phone")
    email = models.EmailField(max_length=255, verbose_name="Email")
    status_contact = models.BooleanField(verbose_name="Status contact", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table="register_voucher"
        verbose_name="Đăng ký nhận voucher"
        verbose_name_plural="Đăng ký nhận voucher"
    
    def __str__(self) -> str:
        return f'{self.full_name}'





    











