"""
URL configuration for StudentDBModelProject7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from StudentDBApp import views;
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentview/', views.studentview),
    path('studenthomepage/', views.student_homepage),
    path('studentinputview/', views.studentinputview),
    path('studinputverifyview/',views.studentinputverifyview),
    path('studentinputview2/', views.studentinputview2),
    path('studentloginpage/', views.studentloginpageview),
    path('studentloginverifypage/', views.studentloginverifypageview),
    path('studentfeedback/', views.feedbackview),
    re_path('^.*$', views.student_homepage),
]
