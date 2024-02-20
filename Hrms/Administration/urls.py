from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('Administration',views.administration,name="Administration"),
    path('All_emps',views.All_emps,name="All_emps"),
     path('add_new',views.add_new,name="add_new"),
    path('update/<str:First_Name>/',views.update_employee,name="Update_Emp"),
    path('confirm_delete/<str:First_Name>/', views.remove_employee, name='confirm_delete'),

   
    

]