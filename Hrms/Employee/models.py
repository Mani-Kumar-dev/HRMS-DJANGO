from django.db import models

# Create your models here.
class Employee_details(models.Model):
    image=models.ImageField(upload_to="images",null=True,blank=True)
    First_Name=models.CharField(max_length=50,null=True)
    Last_Name=models.CharField(max_length=50,null=False)
    Emp_Id=models.IntegerField(default=0)
    Designation=models.CharField(max_length=100)
    Contact=models.BigIntegerField()
    Email=models.CharField(max_length=150)
    Location=models.CharField(max_length=100)
    Salary=models.BigIntegerField(default=0)
   

    def __str__(self):
        return self.First_Name
    # class Payslips(models.Model):
    #     employee=models.ForeignKey(Employee_details,)
    #     Department = models.CharField(max_length=50)
    #     Days_Worked = models.IntegerField(default=0)
    #     Bank_Account = models.BigIntegerField(default=0)
    #     OverTime = models.IntegerField()
    #     LOP = models.IntegerField()