from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Courses
from . models import User
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


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
            redirect('page_of_teacher')
        if user is not None and not user.is_proffesor:  # Assuming 'is_professor' is a boolean field on your user model
                login(request, user)  # Log the user in
                redirect('page_of_student')
        
# def page_of_teacher(request):
#     email = request.POST.get('email')
#     password = request.POST.get('password')

#     if not email or not password:
#         return HttpResponse('Missing email or password')

#     # Authenticate the user using Django's built-in authentication system
#     user = authenticate(request, email=email, password=password)

#     if user is not None and user.is_proffesor:  # Assuming 'is_professor' is a boolean field on your user model
#         login(request, user)  # Log the user in
#         context = {
#             'user': user,
#             'email': email,
#             'teacher': 'no',
#         }
#         return render(request, 'student_display/home.html', context)
#     else:
#         # If the user authentication failed or they are a professor
#         return HttpResponse('Login failed')


#     return HttpResponse('Invalid request method')

# @require_POST  # Ensures that this view only accepts POST requests
# def page_of_student(request):
#     # Extract email and password from the request
#     email = request.POST.get('email')
#     password = request.POST.get('password')

#     if not email or not password:
#         return HttpResponse('Missing email or password')

#     # Authenticate the user using Django's built-in authentication system
#     user = authenticate(request, email=email, password=password)

#     if user is not None and not user.is_proffesor:  # Assuming 'is_professor' is a boolean field on your user model
#         login(request, user)  # Log the user in
#         context = {
#             'user': user,
#             'email': email,
#             'teacher': 'yes',
#         }
#         return render(request, 'student_display/home.html', context)
#     else:
#         # If the user authentication failed or they are a professor
#         return HttpResponse('Login failed')



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