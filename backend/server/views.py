from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    if request.method =='GET':
        return render(request,'home.html')

def about(request):
    if request.method =='GET':
        return render(request,'about.html')