from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name='home'),
    path('/shop', shop,name='shop'),
    path('/aboutus', aboutus,name='aboutus'),
    path('/faq', faq,name='faq'),
    path('/ordernow', ordernow,name='ordernow'),
]