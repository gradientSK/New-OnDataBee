from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.success(request, ('there was an error logging in, try again...'))
            return redirect('/members/user_login')
    else:
        return render(request, 'member_ship/login_view.html')

    # return render(request, 'member_ship/login_view.html', {})
