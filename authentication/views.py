from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    # return HttpResponse("This is the homepage") returning httpResponse
    return render(request, 'authentication/index.html')

def register(request):
    return render(request, 'authentication/register.html')

def log_in(request):
    return render(request, 'authentication/my-login.html')

def dashboard(request):
    return render(request, 'authentication/dashboard.html')
