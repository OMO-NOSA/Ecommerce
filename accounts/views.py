from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('list')
        else:
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2 :
            if User.objects.filter(username=username).exist():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exist():
                    messages.error(request, 'Email addressed is being used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        first_name = first_name, last_name=last_name,username = username,
                        email = email, password = password, password2=password2
                            )
                    user.save()
                    messages.success(request, 'Registration Successful, proceed to login')
                    return redirect('login')
        else:
            messages.error(request, 'password does not match')
            return redirect('register')
    
    return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'you are now logged out')
        return redirect('list')
            



