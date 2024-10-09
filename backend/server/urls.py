from django.urls import path
from . views import home, about
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns

urlpatterns = [
    path('',home,name=  'home'),
    path('about/',about,name=  'about'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns  += staticfiles_urlpatterns()  
