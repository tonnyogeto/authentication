from django.shortcuts import render, redirect
from . forms import CreateUserForm





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
    return render(request, 'authentication/my-login.html')

def dashboard(request):
    return render(request, 'authentication/dashboard.html')
