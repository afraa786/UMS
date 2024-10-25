from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _



class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=500)
    username = None
    is_active = models.BooleanField(default=True)  # Default to True for active users
    is_staff = models.BooleanField(default=False)  # Add is_staff field if missing
    is_proffesor = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()



class Courses(models.Model):
    image = models.ImageField( upload_to=  'courses', null=True, blank=True)
    name =  models.CharField(max_length=100)
    description = models.TextField()
    fees = models.DecimalField(max_digits=15, decimal_places=2)
    course_domain = models.CharField( max_length=50)


    def __str__(self):
        return self.name
    


class Profile(models.Model):
    profile_image = models.ImageField( upload_to='profile/', height_field=None, width_field=None, max_length=None, null=True , blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.TextField(null=True, blank=True)
    branch = models.TextField(_("Branch"),  null=True, blank=True)
    subject = models.TextField(_("Subject"),   null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number= PhoneNumberField(null =  True, blank = True)

    def __str__(self):
        return self.user.email
    


