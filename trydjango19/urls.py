"""trydjango19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
    https://github.com/codingforentrepreneurs/Guides/blob/master/all/common_url_regex.md
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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.post_list, name="index"),
    url(r'^posts/$', views.post_list, name="posts"),
    url(r'^posts/create/$', views.post_create, name="create"),
    url(r'^posts/(?P<slug>.*)/$', views.post_detail, name="detail"),
    url(r'^posts/(?P<id>\d+)/edit/$', views.post_update, name="update"),
    url(r'^posts/(?P<id>\d+)/delete/$', views.post_delete, name="delete"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
