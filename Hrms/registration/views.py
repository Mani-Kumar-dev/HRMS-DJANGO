from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm,Admin_SignUpForm
from django.contrib.auth import authenticate,login

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['c_Password']
            
            if password != confirm_password:
                # user = User.objects.create_user(username=username, password=password)
                # user.save()
                messages.info(request,"Password not Matched")
                return redirect('/Signup')
            try:
                if User.objects.filter(username=username):
                    messages.info(request,"UserName already taken")
                    return redirect('/Signup')
            except Exception as identifier:
                pass
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.info(request,"Succesfully Signed")
            return redirect('/login', {'form': form,})
    else:
        form = SignUpForm()
    return render(request, 'Signup.html', {'form': form})


def login(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        myuser=authenticate(request,username=username,password=password)
        if myuser is not None:
            # login(request,myuser)
            messages.success(request,'Login Successfully')
            return redirect(f'Employee/{username}')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/login')
    return render(request,"Login.html")

# def handlelogout(request):
#     logout(request)
#     messages.success(request,"Logout Successfully")
#     return redirect('/login')

def Admin_sign(request):
    if request.method == 'POST':
        form = Admin_SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['c_Password']
            
            if password != confirm_password:
                # user = User.objects.create_user(username=username, password=password)
                # user.save()
                messages.info(request,"Password not Matched")
                return redirect('/Admin_sign')
            try:
                if User.objects.filter(username=username):
                    messages.info(request,"UserName already taken")
                    return redirect('/Admin_sign')
            except Exception as identifier:
                pass
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.info(request,"Succesfully Signed")
            return redirect('/Admin_login', {'form': form,})
    else:
        form = SignUpForm()
    return render(request,"Admin_sign.html",{'form': form})
     
def Admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        myuser = authenticate(request, username=username, password=password)
        if myuser is not None:
            if myuser.is_staff:  # Assuming staff users are admins
                login(request, myuser)
                messages.success(request, 'Admin Login Successfully')
                return redirect('/Administration')
            else:
                messages.error(request, 'Invalid Admin Credentials')
                return redirect('/Admin_login')
        else:
            messages.error(request, 'Invalid Admin Credentials')
            return redirect('/admin/login')
    return render(request, "Admin_login.html")

