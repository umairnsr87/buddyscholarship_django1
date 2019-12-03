from django.contrib import admin
from django.urls import path,include
from . import views
from .views import PostDetail
#give your urls here
urlpatterns = [

    path('',views.index,name='home'),
    path('blogs/',views.blogs,name='blogs'),
    path('about/',views.about,name='about'),
    path('admissions/',views.admissions,name='admissions'),
    path( '<slug:slug>/', views.PostDetail.as_view(), name='post_detail' ),
]