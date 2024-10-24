from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from . models import Courses, Profile
from . models import User
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import ProfileForm


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
    

def login_user(request):
    if request.method =='GET':
        return render(request,'login.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            return HttpResponse('Missing email or password')

        # Authenticate the user using Django's built-in authentication system
        user = authenticate(request, email=email, password=password)

        if user is not None and user.is_proffesor:  # Assuming 'is_professor' is a boolean field on your user model
            login(request, user)  # Log the user in
            return redirect('page_of_teacher')
        if user is not None and not user.is_proffesor:  # Assuming 'is_professor' is a boolean field on your user model
                login(request, user)  # Log the user in
                return redirect('page_of_student')



def page_of_teacher(request):
    if request.method == 'GET':
        user = request.user
        context = {
            'user': user,
            'email': user.email,
            'teacher': 'yes',
        }
        return render(request, 'teacher_display/home.html')


def page_of_student(request):
    if request.method == 'GET':
        user = request.user
        context = {
            'user': user,
            'email': user.email,
            'teacher': 'no',
        }
        return render(request, 'student_display/home.html')  # Render the home template with the user
    



@login_required(login_url='login/')
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    context = {
        'profile': profile,
        'editable': False,  # Editable status to toggle between viewing and editing
        'project_color': 'rgb(185, 156, 118)',  # Pass your project color scheme
    }
    return render(request, 'profile.html', context)

@login_required(login_url='login/')
def profile_edit(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    context = {
        'form': form,
        'editable': True,  # Toggle to editing mode
        'project_color': 'rgb(185, 156, 118)',  # Pass your project color scheme
    }
    return render(request, 'profile.html', context)
