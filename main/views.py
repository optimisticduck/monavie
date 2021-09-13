from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
import json
from .models import *

# Create your views here.


def home(request):
    if request.method == "POST":
        customerName = request.POST["name"]
        customerMessage = request.POST["message"]

        contactUs = ContactUs_T(
            customerName=customerName, customerMessage=customerMessage
        )
        contactUs.save()
        return render(request, "main/home.html")
    else:
        return render(request, "main/home.html")


def shop(request):
    return render(request, "main/shop.html")


def aboutus(request):
    return render(request, "main/aboutus.html")


def faq(request):
    return render(request, "main/faq.html")


def ordernow(request):
    return render(request, "main/ordernow.html")


def cart(request):
    return render(request, "main/cart.html")


def orderdetails(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        number = request.POST["number"]
        cusaddress = request.POST["cusaddress"]
        delins = request.POST["delins"]
        totalCost = request.POST["totalCost"]
        itemsOrdered = request.POST["itemsOrdered"]

        itemsOrdered = json.loads(itemsOrdered)

        orders = Orders_T(
            fname=fname,
            lname=lname,
            number=number,
            cusaddress=cusaddress,
            delins=delins,
            totalCost=totalCost,
            itemsOrdered=itemsOrdered,
        )

        orders.save()
        return render(request, "main/orderdetails.html")
    else:
        return render(request, "main/orderdetails.html")
