"""main URL Configuration

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
from django.urls import path, include
from donor import views as donor_views
from django.contrib.auth import views as Auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("donate.urls")),
    path('', include("event.urls")),
    path('register/',view=donor_views.register, name='register'),
    path('login/', view=Auth_views.LoginView.as_view(template_name="donor/login.html"), name='login'),
    path('logout/', view=Auth_views.LogoutView.as_view(template_name="donor/logout.html"), name="logout"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        donor_views.activate, name='activate'),
]
