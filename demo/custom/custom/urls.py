"""custom URL Configuration

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
from custom_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customreg',views.cusromRegister,name='customreg'),
    path('login',views.Login,name='login'),
    path('profile',views.profile,name='profile'),
    path('logout',views.Logout,name='logout'),
    path('edit',views.profile_edit,name='edit'),
    path('mark',views.marks,name='mark'),
    path('view_mark',views.view_mark,name='view_mark'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit_score/<int:id>',views.score_edit,name='edit_score'),
    path('password_reset',views.password_reset_request,name='password_reset'),
    path('verify_otp',views.verify_otp,name='verify_otp'),
    path('set_new_password',views.set_new_password,name='set_new_password'),
    
    
]
