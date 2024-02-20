from django.shortcuts import render,get_object_or_404
from . models import Employee_details

# Create your views here.
def Employee(request,First_Name):
    emps = Employee_details.objects.filter(First_Name=First_Name.upper())
    # emps=get_object_or_404(Employee_details,First_Name=First_Name.upper())
    context={"emps":emps}
    return render(request,"employee.html",context)
def Payslips(request,First_Name):
   emps=Employee_details.objects.filter(First_Name=First_Name.upper())
   context={"emps":emps}
   return render(request,"payslips.html",context)

