from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm

# Authenticate models and function
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required





def homepage(request):
    return render(request, 'authentication/index.html')

def register(request):

    form=CreateUserForm

    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save
            return redirect("log-in")
        
    context={'registerform':form}
    return render(request, 'authentication/register.html', context=context)



def log_in(request):
    form =LoginForm()

    if request.method=='POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username =request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context={'loginform':form}

    return render(request, 'authentication/my-login.html', context=context)

@login_required(login_url="log-in")
def dashboard(request):
    return render(request, 'authentication/dashboard.html')

def user_logout(request):
	auth.logout(request)
	return redirect("")
