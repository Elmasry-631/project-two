from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.homepage,name='homepage'),
    path('post/<int:post_id>', views.boards , name = 'boards'),
    path('post/<int:post_id>/new', views.new_post , name = 'new_post'),
]