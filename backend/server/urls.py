from django.urls import path
from . views import home, about,courses
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns

urlpatterns = [
    path('',home,name=  'home'),
    path('about/',about,name=  'about'),
    path('courses/',courses,name=  'courses'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns  += staticfiles_urlpatterns()  
