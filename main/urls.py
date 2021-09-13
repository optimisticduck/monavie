from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("/homeMail", homeMail, name="homeMail"),
    path("/shop", shop, name="shop"),
    path("/aboutus", aboutus, name="aboutus"),
    path("/faq", faq, name="faq"),
    path("/ordernow", ordernow, name="ordernow"),
    path("/cart", cart, name="cart"),
    path("/orderdetails", orderdetails, name="orderdetails"),
]
