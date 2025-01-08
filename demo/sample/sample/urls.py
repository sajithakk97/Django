"""sample URL Configuration

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
from .settings import STATICFILES_DIRS
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.function1,name='index'),
    path('value/<val>',views.pass_value),
    path('add/<int:num1>/<int:num2>',views.add),
    path('vowel_count/<string>',views.count_vowels),
    path('register1',views.register,name='register1'),
    path('display',views.display,name='display'),
    path('delete/<int:id>',views.data_delete,name='delete'),
    path('edit/<int:id>',views.data_edit,name='edit'),
    path('index1',views.index,name='index1'),
    path('user_register',views.userreg,name='userreg'),
    

]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)