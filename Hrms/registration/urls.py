
from django.urls import path
from . import views

urlpatterns = [
   
    path('Signup',views.signup,name="Signup"),
    path('login',views.login,name='login'),
    path('Admin_sign',views.Admin_sign,name="Admin_sign"),
    path('Admin_login',views.Admin_login,name="Admin_login"),


]