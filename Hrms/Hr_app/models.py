from django.db import models


# Create your models here.
class All_Employees(models.Model):
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Emp_Id=models.BigIntegerField(null=True)
    Designation=models.CharField(max_length=50)
    Mobile=models.BigIntegerField()
    Location=models.CharField(max_length=50)
    def __str__(self):
        return self.First_Name  