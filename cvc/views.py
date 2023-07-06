from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.validators import validate_email
import pymysql


def home(request):
    return render(request, 'cvc/home.html')
