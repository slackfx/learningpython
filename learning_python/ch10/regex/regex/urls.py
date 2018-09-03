"""regex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#from django.contrib import admin
#from django.urls import path

from django.conf.urls import include, re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from entries.views import HomeView, EntryListView, EntryFormView

urlpatterns = [
    #path('admin/', admin.site.urls),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^entries/$', EntryListView.as_view(), name='entries'),
    re_path(r'^entries/insert$',
        EntryFormView.as_view(),
        name='insert'),
    re_path(r'^login/$',
        auth_views.LoginView,
        kwargs={'template_name': 'admin/login.html'},
        name='login'),
    re_path(r'^logout/$',
        auth_views.LogoutView,
        kwargs={'next_page': reverse_lazy('home')},
        name='logout'),
    re_path(r'^$', HomeView.as_view(), name='home'),
]
