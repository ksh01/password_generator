from operator import length_hint
from django.shortcuts import render, redirect
from django.http import HttpResponse
from string import ascii_lowercase, ascii_uppercase, digits
from random import choice, shuffle
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def error_404(request, exception):
    return render(request, '404.html')

def password(request):
    charList = list(ascii_lowercase)
    length = int(request.GET.get('length', 12))
    checkLowercase = False
    checkUppercase = False
    checkNumbers = False
    checkSpecial = False
    
    while not(checkLowercase and checkUppercase and checkNumbers and checkSpecial):
        thePassword = []
        checkLowercase = False
        if request.GET.get('uppercase'):
            charList.extend(list(ascii_uppercase))
            checkUppercase = False
        else:
            checkUppercase = True
        if request.GET.get('numbers'):
            charList.extend(list(digits))
            checkNumbers = False
        else:
            checkNumbers = True
        if request.GET.get('special'):
            charList.extend(list('!@#$%^&*()'))
            checkSpecial = False
        else:
            checkSpecial = True
        
        for _ in range(length):
            thePassword.append(choice(charList))
    
        for x in thePassword:
            if checkLowercase and checkUppercase and checkNumbers and checkSpecial:
                break
            if x in ascii_lowercase:
                checkLowercase = True
            elif x in ascii_uppercase:
                checkUppercase = True
            elif x in digits:
                checkNumbers = True
            elif x in '!@#$%^&*()':
                checkSpecial = True

    shuffle(thePassword)
    return render(request, 'generator/password.html', {'password' : "".join(thePassword)})