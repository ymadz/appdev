from django.contrib import admin
from .models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age')
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Course)
