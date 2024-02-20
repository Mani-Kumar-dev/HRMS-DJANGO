
from django.urls import path
from . import views

urlpatterns = [
   
    path('Hr',views.Hr,name="Hr"),
    path('Emp_details',views.Emp_Details,name="Emp_details"),

]