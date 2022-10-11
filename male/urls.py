from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('niff/',views.male_learn),
    #path('nap/',views.male_code),
    path('steam/',views.version_type),    
]
