from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .form import OrderForm, CreateUSerForm


# Create your views here.

def main(request):
    context={}
    return render(request,'rent/index.html',context)

def login(request):
    if request.user.is_authenticated: 
        return redirect('home')
    else:
        form = CreateUSerForm()
        if request.method == 'POST':
            form = CreateUSerForm(request.POST)
            if form.is_valid():
                form.save()
                users = form.cleaned_data.get('username')
                messages.success(request,'Account was created ' + users)

            return redirect('register')
    
    context={'form':form}
    return render(request, 'rent/login.html',context)
    
def register(request):
    if request.user.is_authenticated: 
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login_required(request, user)
        redirect('main')
    else:
        messages.info(request, 'Username Or Password is inccorrect')
       
    context={}
    return render(request, 'rent/register.html',context)

def logoutUser(request):
    logoutUser(request)
    return redirect('login')

@login_required(login_url='register')
def cart(request):

    if request.user.is_authenticated:
        customer=request.user.users
        order1,created= order.objects.get_or_create(user=customer,complete=False)
        items=order1.orderitem_set.all()
    else:
        items=[]
        order1={'get_cart_total':0,'get_cart_items':0}
    context={'items':items,'order':order1}
    return render(request,'rent/cart.html',context)

@login_required(login_url='register')
def checkout(request):
    
    if request.user.is_authenticated:
        customer=request.user.users
        order1,created= order.objects.get_or_create(user=customer,complete=False)
        items=order1.orderitem_set.all()
    else:
        items=[]
        order1={'get_cart_total':0,'get_cart_items':0}
    context={'items':items,'order':order1}
    return render(request,'rent/checkout.html',context)

def renting(request):
    
    if request.user.is_authenticated:
        customer=request.user.users
        order1,created= order.objects.get_or_create(user=customer,complete=False)
        items=order1.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order1={'get_cart_total':0,'get_cart_items':0}
        cartItems= order1['get_cart_items']

    products=jewellery.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'rent/renting.html',context)

def updateItem(request):
    data=json.loads(request.data)
    productId=data['productid']
    action=data['action']

    print('action',action)
    print('productid',productId)

    customer=request.user.users
    product=jewellery.objects.get(groupid=productId)
    order1,created= order.objects.get_or_create(user=customer,complete=False)
    orderItem,created=OrderItem.objects.get_or_create(order=order1,product=product)

    if action=='add':
        orderItem.quantity=(orderItem.quantity+1)
    elif action=='remove':
        orderItem.quantity=(orderItem.quantity-1)

    orderItem.save()

    if orderItem.quantity<=0:
        orderItem.delete()

    return JsonResponse('Item was added',safe=False)