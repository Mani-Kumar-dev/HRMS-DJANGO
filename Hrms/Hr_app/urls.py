from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/',views.index,name="index"),
    path('hr/',views.hr,name="hr"),
    path('All_emps/',views.All_emps,name="All_emps"),
    path('Add_emps/',views.Add_emps,name="Add_emps"),
    path('remove_emps/',views.remove_emps,name="remove_emps"),


    
]