from django.db import models

# Create your models here.
class Course(models.Model):
    course_title = models.CharField(max_length=15,unique=True)    
    file = models.FileField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_title
    
class User(models.Model):
    username = models.CharField(max_length=100)
    emailid =models.EmailField()
    phno = models.IntegerField()    
    collagename = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    course_year = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    