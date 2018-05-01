"""rindus_bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from bank.views import home, person_create, person_update, person_delete, account_create, account_update, \
    account_delete, person_read, account_read

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^oauth/', include('social_django.urls')),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^$', home, name='home'),

    #Crud Person
    url(r'^new_person$', person_create, name='person_create'),
    url(r'^show_person/(?P<pk>\d+)$', person_read, name='person_read'),
    url(r'^edit_person/(?P<pk>\d+)$', person_update, name='person_update'),
    url(r'^delete_person/(?P<pk>\d+)$', person_delete, name='person_delete'),

    #Crud Account
    url(r'^new_account/(?P<pk>\d+)', account_create, name='account_create'),
    url(r'^account_person/(?P<pk>\d+)$', account_read, name='account_read'),
    url(r'^edit_account/(?P<pk>\d+)$', account_update, name='account_update'),
    url(r'^delete_account/(?P<pk>\d+)$', account_delete, name='account_delete'),

]
