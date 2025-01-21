"""student_management URL Configuration

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
from teacher import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',views.register,name='register'),
    path('login',views.Login,name='login'),
    path('view_student',views.view_students,name='view'),
    path('add_student',views.add_student,name='add'),
    path('delete/<int:id>',views.delete_student,name='delete'),
    path('edit/<int:id>',views.edit_student,name='edit'),
    path('profile',views.profile,name='profile'),
    path('logout',views.Logout,name='logout'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('search',views.search,name='search'),
    path('add_mark/<int:id>',views.add_mark,name='add_mark'),
    path('mark/<int:id>',views.marks,name='mark'),

]
