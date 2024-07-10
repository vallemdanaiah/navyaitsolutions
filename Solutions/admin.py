from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Course)
# admin.site.register(User)



class EmployeeAdmin(admin.ModelAdmin):
 list_display = ['username','emailid','collagename','course_year','phno']
 search_fields = ('username','emailid','course_year')
# Register your models here.
admin.site.register(User,EmployeeAdmin) 




