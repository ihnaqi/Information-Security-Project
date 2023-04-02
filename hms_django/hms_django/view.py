from django import http
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect



def index(request):
    return render(request,'index.html')

