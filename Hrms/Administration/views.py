from django.shortcuts import render,redirect, get_object_or_404
from Employee.models import Employee_details
from django.contrib import messages
from Hr.forms import EmployeeDetailsForm

# Create your views here.
def administration(request):
    return render(request,"Administration.html")
def All_emps(request):
    emps=Employee_details.objects.all()
    context={"emps":emps}
    return render(request,"All_Employees.html",context)
def add_new(request):
    if request.method == "POST":
        image=request.FILES.get("image")
        First_Name=request.POST.get("First_Name")
        Last_Name=request.POST.get("Last_Name")
        Emp_Id=request.POST.get("Emp_Id")
        Designation=request.POST.get("Designation")
        Contact=request.POST.get("Contact")
        Email=request.POST.get("Email")
        Location=request.POST.get("Location")
        Salary=request.POST.get("Salary")
        query=Employee_details(First_Name=First_Name,Last_Name=Last_Name,Emp_Id=Emp_Id,Designation=Designation,Contact=Contact,Email=Email,Location=Location,Salary=Salary,image=image)
        query.save()
        messages.success(request,"Successfully Added")
        return redirect("/All_emps")
    elif request.method == "GET":
        return render(request,"Add_new.html")
    else:
       
        messages.error(request,"Unsuccessfull")
        return redirect("/add_new",)
    
def update_employee(request,First_Name):
    emps = get_object_or_404(Employee_details,First_Name=First_Name.upper())
    context={"emps":emps}
    if request.method == "POST":
        image=request.FILES.get,("image")
        First_Name=request.POST.get("First_Name")
        Last_Name=request.POST.get("Last_Name")
        Emp_Id=request.POST.get("Emp_Id")
        Designation=request.POST.get("Designation")
        Contact=request.POST.get("Contact")
        Email=request.POST.get("Email")
        Location=request.POST.get("Location")
        Salary=request.POST.get("Salary")
        query=Employee_details(First_Name=First_Name,Last_Name=Last_Name,Emp_Id=Emp_Id,Designation=Designation,Contact=Contact,Email=Email,Location=Location,Salary=Salary,image=image)
        query.save()
        # Update existing employee details
        # emps.image = request.FILES.get("image")
        # emps.First_Name = request.POST.get("First_Name")
        # emps.Last_Name = request.POST.get("Last_Name")
        # emps.Designation = request.POST.get("Designation")
        # emps.Contact = request.POST.get("Contact")
        # emps.Email = request.POST.get("Email")
        # emps.Location = request.POST.get("Location")
        # emps.Salary = request.POST.get("Salary")
        # emps.save()
        messages.success(request, "Successfully Updated")
        return redirect("/All_emps")
    return render(request, 'update.html',context)


    
    

 

def remove_employee(request, First_Name):
    if First_Name:
        try:  
            emp_to_be_removed =get_object_or_404(Employee_details, First_Name=First_Name.upper())
            emp_to_be_removed.delete()
            messages.success(request, 'Employee successfully deleted.')
            return redirect("/All_emps")
        except:
            messages.error(request, 'Failed to delete employee.')
            return redirect("/All_emps")
   
    return render(request, 'Remove.html')