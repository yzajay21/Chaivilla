"""chaivilla_project URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from menu.views import Menu_view
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse


from home.views import Homepageview
from menu.views import item
#from home.views import BeverageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^$',Menu_view,name='Menu_view'),
    
    url(r'^item/(?P<menu_id>[0-9]+)',item,name='item'),
    url(r'^menu/item/(?P<menu_id>[\w-]+)/$',item,name='item'),

]