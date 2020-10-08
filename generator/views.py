from django.shortcuts import render
from django.http import HttpResponse
from string import ascii_lowercase, ascii_uppercase
import random

# Create your views here.
def home(request):
    return render(request, './generator/home.html',{'password':'1234'})

def password(request):

    characters = list(ascii_lowercase)

    if request.GET.get('uppercase'):
        characters.extend(list(ascii_uppercase))

    if request.GET.get('special'):
        characters.extend(list("!@#$%^&*()_+"))

    if request.GET.get('numbers'):
        characters.extend(list("1234567890"))

    length = int(request.GET.get('length',12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, './generator/password.html',{'password':thepassword})

def about(request):
    return render(request, './generator/about.html')
