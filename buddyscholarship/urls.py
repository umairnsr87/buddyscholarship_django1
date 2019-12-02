from django.contrib import admin
from django.urls import path,include
from . import views

#give your urls here
urlpatterns = [

    path('',views.index,name='home'),
    path('blogs/',views.blogs,name='blogs'),



]