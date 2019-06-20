
from django.contrib import admin
from django.urls import path

from . import views #means from .(this directory) import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.homepage, name='home'), #means we have to define a function calledhome in views it will redirect there

    #we use name so we can use {{%url  % }}#

    path('count/',views.count, name ='count'), #we have to define a fucntion called as count in views {% %} for


    path('about/',views.about, name ='aboutUs'),


]
