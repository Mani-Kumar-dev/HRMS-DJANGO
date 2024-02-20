from django.shortcuts import render

# Create your views here.
def Base(request):
    return render(request,"index.html")
def home(request):
    return render(request,"home.html")