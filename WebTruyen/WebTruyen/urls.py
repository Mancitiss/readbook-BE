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
from django.urls import path, include, re_path
from api import views
from .com.moduleCrawlerr.init import InitCraler
import thread6
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="WebTruyenApi",
        default_version='v1',
        description="API for WebTruyen",
        contact=openapi.Contact(email='20510615@gm.uit.edu.vn'),
        license=openapi.License(name="Phan Thi Linh"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin', admin.site.urls),
    path('api/chapter/', views.Chapter_list),
    path('api/story/', views.Story_list),
    path('api/', include('backend.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui (cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui ('redoc', cache_timeout=0), name='schema-redoc'),
]


@thread6.threaded()
def thread_crawler_story():
    print('run thread')
    InitCraler.init()
try:
   
    thread6.run_threaded(thread_crawler_story)
except:
    print("Error: unable to start thread")
