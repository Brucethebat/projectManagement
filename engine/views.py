from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='engine:loginurls')
def homeView(request):
    return render(request, 'engine/dashboard.html') 


@login_required(login_url='engine:loginurls')
def teachersView(request):
    return render(request, 'engine/teachers.html')

def studentsView(request):
    return render(request, 'engine/students.html')

def addstudentView(request):
    return render(request, 'engine/addstudent.html')


def editstudentView(request):
    return render(request, 'engine/editstudent.html')


def aboutstudentView(request):
    return render(request, 'engine/aboutstudent.html')


def calendarView(request):
    return render(request, 'engine/calendar.html')

def settingView(request):
    return render(request, 'engine/setting.html')


def changepView(request):
    return render(request, 'engine/changep.html')


def blogView(request):
    return render(request, 'engine/blog.html')


def blogviewView(request):
    return render(request, 'engine/blogview.html')


def addblogView(request):
    return render(request, 'engine/addblog.html')


def editblogView(request):
    return render(request, 'engine/editblog.html')


def chatView(request):
    return render(request, 'engine/chat.html')


def myprofileView(request):
    return render(request, 'engine/myprofile.html')


def editproView(request):
    return render(request, 'engine/editpro.html')


def ssettingView(request):
    return render(request, 'engine/ssetting.html')


def loginView( request):
    
    return render(request, 'engine/login.html')


def homeView(request):
    return render(request, 'engine/home.html')

