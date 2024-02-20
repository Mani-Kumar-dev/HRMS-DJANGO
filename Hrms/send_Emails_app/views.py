# from django.shortcuts import render,get_object_or_404,redirect
# from django.core.mail import EmailMessage
# from Employee.models import Employee_details
# from Hr_app.models import All_Employees
# from django.contrib import messages

# # Create your views here.
# def send_payslips(request,First_Name):
#     emps = Employee_details.objects.filter(First_Name=First_Name.upper())
#     # emps=get_object_or_404(Employee_details,First_Name=First_Name.upper())
#     context={"emps":emps}
#     return render(request,'send_paysilps.html',context)

# def add_payslips(request):
#     if request.method == 'POST':
#         First_Name=request.POST.get('First_Name')
#         Last_Name=request.POST.get('Last_Name')
#         Emp_Id=request.POST.get('Emp_Id')
#         Designation=request.POST.get('Designation')
#         query=All_Employees(First_Name=First_Name,Last_Name=Last_Name,Emp_Id=Emp_Id,Designation=Designation)
#         query.save()

#         messages.info(request,"Successfully Added....")
#         return redirect('/send_payslips')
#     elif request.method == "GET":
#         return render(request,"generate_paysilps.html")
#     else:
#         messages.info(request,"Unsuccesfull")
#         return redirect('/gen_payslips')
