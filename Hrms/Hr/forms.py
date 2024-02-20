from django import forms
from Employee.models import Employee_details

class EmployeeDetailsForm(forms.ModelForm):
    class Meta:
        model = Employee_details
        fields = ['image', 'First_Name', 'Last_Name', 'Emp_Id', 'Designation', 'Contact', 'Email', 'Location', 'Salary']
        # Specify the fields you want to include in the form for updating

