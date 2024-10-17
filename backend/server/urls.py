from django.urls import path
from . views import home, about,courses, login_user, page_of_teacher, page_of_student
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns

urlpatterns = [
    path('',home,name=  'home'),
    path('about/',about,name=  'about'),
    path('courses/',courses,name=  'courses'),
    path('login/',login_user,name=  'login'),
    path('home_teacher/',page_of_teacher,name=  'page_of_teacher'),
    path('home_student/',page_of_student,name=  'page_of_student'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns  += staticfiles_urlpatterns()  
