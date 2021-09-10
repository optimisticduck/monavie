from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def shop(request):
    return render(request, 'main/shop.html')

def aboutus(request):
    return render(request, 'main/aboutus.html')

def faq(request):
    return render(request, 'main/faq.html')

def ordernow(request):
    return render(request, 'main/ordernow.html')