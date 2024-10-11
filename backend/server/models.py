from django.db import models

class Courses(models.Model):
    image = models.ImageField( upload_to=  'courses', null=True, blank=True)
    name =  models.CharField(max_length=100)
    description = models.TextField()
    fees = models.DecimalField(max_digits=15, decimal_places=2)
    course_domain = models.CharField( max_length=50)


    def __str__(self):
        return self.name