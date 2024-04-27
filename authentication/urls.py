from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name=""),
    path('register', views.register, name="register"),
    path('log-in', views.log_in,name="log-in"),
    path('dashboard', views.dashboard, name="dashboard"),

]
