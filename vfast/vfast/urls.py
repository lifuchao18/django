"""vfast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from acces.views import index
from acces.views import html
from acces.views import server
from acces.views import student
from acces.views import studens
from acces.views import studens_info
from acces.views import students
from acces.views import delete_student
from acces.views import student_info
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index),
    url(r'^html/$',html),
    url(r'^server/$',server),
    url(r'^student/$',student),
    url(r'^studens/$',studens),
    url(r'^students/$',students,name='students'),
    url(r'^student/delete/(?P<_id>\d+)/$',delete_student,name='delete_student'),
    url(r'^student/info/(?P<_id>\d+)/$',student_info,name='student_info')
]
