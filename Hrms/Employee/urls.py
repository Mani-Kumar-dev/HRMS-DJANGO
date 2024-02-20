from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('Employee/<str:First_Name>/',views.Employee,name="Employee"),
    path('payslips/<str:First_Name>/',views.Payslips,name="payslips"),

    

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)