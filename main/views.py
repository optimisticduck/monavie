from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    if request.method == 'POST':
        customerName = request.POST['name']
        customerMessage = request.POST['message']
        
        contactUs = ContactUs_T(customerName=customerName,customerMessage=customerMessage)
        contactUs.save()
        return render(request, 'main/home.html')
    else:
        return render(request, 'main/home.html')

def shop(request):
    return render(request, 'main/shop.html')

def aboutus(request):
    return render(request, 'main/aboutus.html')

def faq(request):
    return render(request, 'main/faq.html')

def ordernow(request):
    return render(request, 'main/ordernow.html')