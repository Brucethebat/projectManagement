from django.shortcuts import render

def homeView(request):
    return render(request, 'engine/dashboard.html') 



def teachersView(request):
    return render(request, 'engine/teachers.html')