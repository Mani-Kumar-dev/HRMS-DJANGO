from django.shortcuts import render,redirect, get_object_or_404
from Employee.models import Employee_details



# Create your views here.
def Hr(request):
    return render(request,"hr.html")

def Emp_Details(request):
    emps=Employee_details.objects.all()
    context={"emps":emps}
    return render(request,"emp_details.html",context)

  