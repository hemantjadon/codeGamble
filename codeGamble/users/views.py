from django.shortcuts import render
import os
# Create your views here.

def HomePage(request):
    x = os.environ.get('DJANGO_SECRET_KEY')
    return render(request,'Home/homepage.html',{"key":x})