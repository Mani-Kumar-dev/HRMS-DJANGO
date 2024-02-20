from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import All_Employees

# Create your views here.
def index(request):
    return render(request,"index.html")

def hr(request):
    return render(request,"hr.html")
def Paysilps(request):
    return render(request,"Paysilps.html")
def All_emps(request):
    emps=All_Employees.objects.all()
    context={'emps':emps}   

    return render(request,"All_emps.html",context)
def Add_emps(request):
    if request.method == 'POST':
        First_Name=request.POST.get('First_Name')
        Last_Name=request.POST.get('Last_Name')
        Emp_Id=request.POST.get('Emp_Id')
        Designation=request.POST.get('Designation')
        Mobile=request.POST.get('Mobile')
        Location=request.POST.get('Location')
        query=All_Employees(First_Name=First_Name,Last_Name=Last_Name,Emp_Id=Emp_Id,Designation=Designation,Mobile= Mobile,Location=Location)
        query.save()

        messages.info(request,"Successfully Added....")
        return redirect('/Add_emps')
    elif request.method == "GET":
        return render(request,"Add_emps.html")
    else:
        messages.info(request,"Unsuccesfull")
        return redirect('/Add_emps')

def remove_emps(request):
    return render(request,"remove_emps.html")