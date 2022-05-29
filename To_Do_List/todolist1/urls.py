from django.contrib import admin
from django.urls import path, include
from todolist1 import views

urlpatterns = [
   path('',views.index_page,name="home"),
   # path('setincrementto0/',views.set_increment_0),
]
