
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .form import  CreateUSerForm


def main(request):
    context={}
    return render(request,'rent/index.html',context)



def rent(request):
    products=jewellery.objects.all()
    context={'products':products}
    return render(request,'rent/renting.html',context)
