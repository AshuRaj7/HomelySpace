from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def logout_view(request):
    logout(request)
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('listing') 
    else:
        form = SignupForm()
    return render(request, 'login.html', {'form': form})

def login_view(request):
    if request.method=='POST':
        usr=request.POST.get('username')
        pwd=request.POST.get('password')
        user=fetch_user_by_username(usr)
        if user:
            if user.password==pwd:
                login(request,user)
                return redirect('listing')
            else:
                messages.add_message(request,messages.ERROR,'Invalid Credentials')
                return redirect('login')
        else:
            messages.add_message(request,messages.ERROR,'User Does Not Exist')
            return redirect('login')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

def fetch_user_by_username(usr):
    User=get_user_model()
    try:
        user=User.objects.get(email=usr)
        return user
    except User.DoesNotExist:
        return None