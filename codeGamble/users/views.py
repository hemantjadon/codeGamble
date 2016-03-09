from django.shortcuts import render
import os
# Create your views here.

def HomePage(request):
    return render(request,'Home/homepage.html',{})