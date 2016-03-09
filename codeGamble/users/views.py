from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from users.models import *
from users.forms import RegisterForm

# Create your views here.

def HomePage(request):
    if request.user.is_anonymous():
        return render(request,'Home/homepage.html',{})
    else:
        return redirect(reverse('register_page'))

def InstructionsPage(request):
    return render(request,"Home/instructionspage.html",{})
    
@login_required(login_url='/')
def RegisterPage(request):
    if request.method == 'GET':
        if request.user.registered == True:
            return redirect(reverse('questions_page'))
        register_form = RegisterForm()
        return render(request,"Home/registerpage.html",{"register_form":register_form})
    elif request.method == 'POST':
        register_form = RegisterForm(request.POST)
        
        if register_form.is_valid():
            user = request.user
            team_name = register_form.cleaned_data['team_name']
            first_member = register_form.cleaned_data['first_member']
            second_member = register_form.cleaned_data['second_member']
            userProfile = UserProfile.objects.create(user=user,team_name=team_name,first_member=first_member,second_member=second_member)
            userProfile.save()
            user.registered = True
            user.save()
            return redirect(reverse('questions_page'))
        else:
            return render(request,"Home/registerpage.html",{"register_form":register_form})