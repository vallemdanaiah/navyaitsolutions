from django.shortcuts import render,get_object_or_404
from django.http import FileResponse
from .models import User, Course
# Create your views here.
def index(request):
    course = Course.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        emailid = request.POST.get('emailid')
        phno = request.POST.get('phno')
        collagename = request.POST.get('collagename')
        course = request.POST.get('course')
        username = request.POST.get('username')
        course_year = request.POST.get('course_year')
        User(
            username = username,
            emailid = emailid,
            phno = phno,
            collagename = collagename,
            course = course,
            course_year = course_year,
            ).save()
        return render(request,'base.html',{'course':'course',})
    else:
        return render(request,'base.html',{'course':'course',})
        




