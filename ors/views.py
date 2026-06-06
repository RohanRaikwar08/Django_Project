from django.http import HttpResponse
from django.shortcuts import render, redirect


def test_ors(request):
    return HttpResponse('<h1> welcome to my ors app </h1>')


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    if request.method == 'POST':
        print(request.POST.get('firstName'))
        print(request.POST.get('lastName'))
        print(request.POST.get('loginID'))
        print(request.POST.get('password'))
        print(request.POST.get('dob'))
        print(request.POST.get('address'))

    return render(request, 'registration.html')


def user_signin(request):
    if request.method == 'POST':
        operation = request.POST.get('operation', '')
        if operation == 'signin':
            print(request.POST.get('login ID'))
            print(request.POST.get('password'))
        if operation == 'signup':
            return redirect('/ors/signup/')

    return render(request, 'login.html')
