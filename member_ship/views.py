from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm


def user_login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/d/dashboard')
        else:
            messages.success(request, ('there was an error logging in, try again...'))
            return redirect('/m/user_login')
    else:
        return render(request, 'member_ship/login_view.html')

def user_logout (request):
    logout(request)
    messages.success(request, ('you were logged out ...'))
    return redirect('/')



#add log out function later
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login (request, user)
            messages.success(request, ('registeration, successfull'))
            return redirect('/d/dashboard')
    else:
        form = RegisterUserForm()
            
    return render(request, 'member_ship/signup_view.html', {
        'form': form ,
    })
