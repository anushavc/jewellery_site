from django.shortcuts import render
from .models import *
# Create your views here.

def main(request):
    context={}
    return render(request,'rent/index.html',context)

def cart(request):
    context={}
    return render(request,'rent/cart.html',context)


def checkout(request):
    context={}
    return render(request,'rent/checkout.html',context)

def renting(request):
    products=jewellery.objects.all()
    context={'products':products}
    return render(request,'rent/renting.html',context)
