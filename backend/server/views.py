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
        
        # Try to get the profile for the user
        try:
            profile = Profile.objects.get(user=user)
            context = {
                'profile': profile,
                'user': user,
                'email': user.email,
                'teacher': 'yes',
            }
        except Profile.DoesNotExist:
            # Handle the case where the profile does not exist
            context = {
                'profile': None,  # or handle it however you prefer
                'user': user,
                'email': user.email,
                'teacher': 'yes',
            }
            # Optionally, you could also set a message or redirect
            # messages.error(request, "Profile not found.")
        
        return render(request, 'teacher_display/home.html', context)


def page_of_student(request):
   if request.method == 'GET':
        user = request.user
        
        # Try to get the profile for the user
        try:
            profile = Profile.objects.get(user=user)
            context = {
                'profile': profile,
                'user': user,
                'email': user.email,
                'teacher': 'no',
            }
        except Profile.DoesNotExist:
            # Handle the case where the profile does not exist
            context = {
                'profile': None,  # or handle it however you prefer
                'user': user,
                'email': user.email,
                'teacher': 'no',
            }
            # Optionally, you could also set a message or redirect
            # messages.error(request, "Profile not found.")
        
        return render(request, 'teacher_display/home.html', context)




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
        form = ProfileForm(request.POST, request.FILES, instance=profile)  # Add request.FILES to handle image upload
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    
    context = {
        'form': form,
        'editable': True,
        'project_color': 'rgb(185, 156, 118)',
    }
    return render(request, 'profile.html', context)

def LogoutPage(request):
    logout(request)
    return redirect('login')