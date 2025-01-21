"""session URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('student_register',views.student_register,name='studentreg'),
    path('teacher_register',views.teacher_register,name='teacherreg'),
    path('login',views.logins,name='login'),
    path('view_teacher',views.view_teachers,name='view_teacher'),
    path('view_student',views.view_students,name='view_student'),
    path('logout1',views.logout,name='logout1'),
    path('logout2',views.logout_student,name='logout2'),
    path('profile',views.userprofile,name='profile'),
    path('logout_admin',views.logout_admin,name='logout_admin'),
    path('set_status/<int:id>',views.set_status,name='set_status'),
    path('set_status1/<int:id>',views.set_status_teacher,name='set_status1'),
]
