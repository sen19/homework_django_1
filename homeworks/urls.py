"""homeworks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from app.views import main, dynamic, dynamic_archieve, users, regex, test_number

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('articles/', main),
    path('articles/archive', main),
    path('users', main),
    path('article/<int:article_number>', dynamic),
    path('article/<int:article_number>/archive', dynamic_archieve),
    path('users/<int:user_number>', users),
    re_path(r'^(?P<text>([a-f]|[0-9]){4}-[a-zA-Z][0-9]{6}$)', regex),
    re_path(r'^(?P<text>(?:050|093|067|096|097|098|066|095|099|063|073|093|091|092|094)[0-9]{7}$)', test_number)
    
]
