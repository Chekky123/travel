from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['password2']

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')

            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                            password=password)
            user.save();
            messages.info(request, 'USER REGISTERED')
            print('USER REGISTERED')

    else:
        messages.info(request, 'password did not match!!')
        return redirect('register')
        return redirect('/')
    return render(request, "register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
