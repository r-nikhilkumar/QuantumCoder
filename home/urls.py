from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name="home"),
    path("about",views.about, name="about"),
    path("moredetails", views.moredetails, name="moredetails"),
    path("developer",views.developer, name="developers"),
    path("customize",views.dashboard, name="customize"),
]
