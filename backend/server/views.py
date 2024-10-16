from django.shortcuts import render
from django.http import HttpResponse
from . models import Courses
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    if request.method =='GET':
        courses =  Courses.objects.all()
        context = {
            'courses': courses,
            }
        return render(request,'home.html', context)

def about(request):
    if request.method =='GET':
        return render(request,'about.html')
    
def courses(request):
    if request.method =='GET':
        courses =  Courses.objects.all()
        context = {
            'courses': courses,
            }
        return render(request,'courses.html',context)