"""WebStory URL Configuration

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
from django.urls import path
from api import views
from .com.moduleCrawlerr.init import InitCraler
import thread6
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/chapter/', views.Chapter_list),
    path('api/story/', views.Story_list)
]


@thread6.threaded()
def thread_crawler_story():
    print('run thread')
    InitCraler.init()
try:
   
    thread6.run_threaded(thread_crawler_story)
except:
    print("Error: unable to start thread")
