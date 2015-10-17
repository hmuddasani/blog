from django.shortcuts import HttpResponseRedirect, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import MyUser, MyUserManager
from .forms import RegisterForm
from .forms import LoginForm

# Create your views here.

def registration_complete(request):
   return render(request, 'registration_complete.html', {}) 
   

def register(request):
   form = RegisterForm(request.POST or None)
   if form.is_valid():
	  username = form.cleaned_data['username']
	  email = form.cleaned_data['email']
	  password = form.cleaned_data['password2']
	  MyUserManager.objects.create_user(username=username, password=password, email=email) # Creates User with username and password
	  #return HttpResponseRedirect("registration_complete")
   context = {
			"form": form,
			   }
   return render(request, 'register.html', context)
   
   
   
def auth_login(request):
  form = LoginForm(request.POST or None)
  print "UserName"
  #next_url=request.GET.get('next')
  print form.is_valid()
  if form.is_valid():
     UserName = form.cleaned_data['UserName']
     Password = form.cleaned_data['Password']
     user=authenticate(UserName=UserName, Password=Password)
     print "UserName", UserName
     if user is not None:
			print "user", user
			login(request, user)
			#if next_url is not None:
				#return HttpResponseRedirect(next_url)
			return HttpResponseRedirect("home")
  context = { 
             "form" : form,
			 }
  return render(request, 'login.html', context)
  
  
def auth_logout(request):
   logout(request)
   return HttpResponseRedirect('/')