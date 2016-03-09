from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt, csrf_protect
from django.core.exceptions import SuspiciousOperation,ObjectDoesNotExist
from users.models import *
from questions.models import *
from questions.forms import AnswerForm
from django.conf import settings
import os
from datetime import datetime
from django.utils.dateformat import format

# Create your views here.
@login_required(login_url='/')
def QuestionsPage(request):
    if request.user.registered:
        if request.user.user_profile.win == True:
            return redirect(reverse('win_page'))
        else:
            if request.method == 'GET':
                try:
                    question = Question.objects.get(current=True)
                except ObjectDoesNotExist:
                    request.user.user_profile.win = True
                    request.user.user_profile.save()
                    return redirect(reverse('win_page'))
                answer_form = AnswerForm()
                return render(request,'Questions/questionspage.html',{"question":question,"answer_form":answer_form})
            elif request.method == 'POST':
                question = Question.objects.get(current=True)
                answer_form=AnswerForm(request.POST,request.FILES)
                if answer_form.is_valid():
                    recieved_file = request.FILES['file']
                    sample_file = open(os.path.join(settings.BASE_DIR,'files/output/'+question.title+".txt"), 'rb')
                    flag = True
                    line1 = recieved_file.readline()
                    
                    line2 = sample_file.readline()
                    while line1 != bytes('','utf-8') or line2 != bytes('','utf-8'):
                        print(line1,line2)
                        if line1 != line2:
                            flag = False
                            break
                        line1 = recieved_file.readline()
                        line2 = sample_file.readline()
                    print(flag)
                    sample_file.close
                    if flag:
                        request.user.user_profile.win = True
                        request.user.user_profile.time_counter = int(format(datetime.now(), 'U'))
                        request.user.user_profile.save()
                        return redirect(reverse('win_page'))
                    else:
                        answer_form.add_error('file',"Oops, This is not the answer we expected")
                        return render(request,'Questions/questionspage.html',{"question":question,"answer_form":answer_form})
                else:
                    return render(request,'Questions/questionspage.html',{"question":question,"answer_form":answer_form})
                    
    else:
        return redirect(reverse('register_page'))
        

@login_required(login_url='/')
def WinPage(request):
    if (request.user.user_profile.win == True):
        return render(request,'Home/winpage.html',{})
    else:
        return redirect(reverse('questions_page'))
        
        
def Leaderboard(request):
    if request.user.is_superuser:
        return render(request,'Questions/leaderboard.html',{})
    else:
        return HttpResponse('You are not authorized to view this page')

def LeaderboardGet(request):
    if request.user.is_superuser:
        leaders_obj = UserProfile.objects.filter(win=True)
        leaders = []
        for obj in leaders_obj:
            x = {}    
            x['id'] = obj.user.pk
            x['name'] = obj.team_name
            leaders.append(x)
        return JsonResponse({"list":leaders})
    else:
        return HttpResponse('You are not authorized to view this page')
 
def MoveNext(request):
    users = UserProfile.objects.all()
    for user in users:
        user.win = False
        user.time_counter = 0
        user.save()
    curr_ques = Question.objects.get(current=True)
    if curr_ques.next != None:
        curr_ques.next.current = True
        curr_ques.next.save()
        curr_ques.current = False
        curr_ques.save()
    curr_ques.current = False
    curr_ques.save()
    return redirect(reverse('leaderboard'))