from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .forms import CreateUserForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout, get_user_model
from django.http import HttpResponseBadRequest, JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import AnswerForm
from .models import Question, Answer, Level
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control

@login_required(login_url='question')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def question(request,pk):
    levelscore=Level.objects.get(user=request.user)
    if levelscore.level>=16:
        return render(request,'completed.html')
    que=Question.objects.get(pk=pk)
    ans=str(Answer.objects.get(question=que))
    if pk<levelscore.level:
        return HttpResponseRedirect(reverse('question', args=(levelscore.level,)))
    if request.method=='POST':
        form=AnswerForm(request.POST)
        if pk<levelscore.level:
            return HttpResponseRedirect(reverse('question', args=(levelscore.level,))) 
        if form.is_valid():
            ans1 = form.cleaned_data.get("Answer")
            if ans1==ans:
                levelscore.score=levelscore.score+10
                levelscore.level=levelscore.level+1
                levelscore.save()
                #form.save()
                return HttpResponseRedirect(reverse('question', args=(levelscore.level,))) 
            else:
                messages.success(request,'Incorrect Answer, Try Again!')
                return HttpResponseRedirect(reverse('question', args=(levelscore.level,))) 
    else:
        form=AnswerForm()
    return render(request,'question.html', {'que':que,'form':form,'levelscore':levelscore})  



def leaderboard(request):
    levelscore=Level.objects.all().order_by('-score')
    return render(request,'leaderboard.html',{'levelscore':levelscore })
   

@login_required(login_url='completed')
def completed(request):
    return render(request,'completed.html')


@login_required(login_url='frontpage')
def frontpage(request):
    levelscore=Level.objects.get(user=request.user)
    return render(request,'frontpage.html',{'levelscore':levelscore })  


def home(request):
    user=request.user
    if user.is_authenticated:
        return redirect('frontpage') 
    else:
        return render(request,'base.html')



def register(request):
    user=request.user
    if user.is_authenticated:
        return redirect('frontpage') 
    else:
        if request.method == 'POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                u = User.objects.get(username=user)
                Level.objects.create(user=u)
                messages.success(request,'Account was created for '+ user)
                return redirect('loginpage')
        else:
            form=CreateUserForm()    
        context = {'form':form }    
        return render(request,'register.html',context)

def loginpage(request):
    user = request.user
    if user.is_authenticated:
        return redirect('frontpage') 
    else:
        next = request.GET.get('next')
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            login(request, user)
            if next:
                return redirect(next)
            return redirect('frontpage')
        
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)

def logoutpage(request):
    logout(request)
    return redirect('home')