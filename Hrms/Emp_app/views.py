from django.shortcuts import render

# Create your views here.
def Employee(request):
    return render(request,'employee.html')