"""
URL configuration for students_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from students_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home.html"),
    path('home',views.home,name="home.html"),
    path('register',views.register,name="register.html"),
    path('profile',views.profile,name="profile.html"),
    path('stdprofile/<int:id>',views.stdprofile,name="stdprofile.html"),
    path('delete/<int:id>',views.delete),
    path('deleteall',views.deleteall),
    path('edit/<int:id>',views.edit,name="edit.html"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
