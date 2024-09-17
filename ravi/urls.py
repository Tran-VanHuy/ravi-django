"""
URL configuration for ravi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from ui.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name="landing-page"),
    path('du-an/<id>/', ProjectDetailPage.as_view(), name="project-detail"),
    path('du-an', ProjectListPage.as_view(), name="project-list"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('register-voucher-ajax', RegisterVoucher, name="register-voucher-ajax"),
    path('tuyen-dung', JobListPage.as_view(), name="job-list"),
    path('tuyen-dung/<id>', JobOpening.as_view(), name="job-opening"),
    path('ve-chung-toi/<id>', AboutPage.as_view(), name="about"),
    path('linh-vuc/<id>', ActionDetailPage.as_view(), name="action-detail"),
]

urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
