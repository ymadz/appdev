from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def crud(request):
    return render(request, 'crud.html')

def student_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_view')
    else:
        form = StudentForm()
    
    students = Student.objects.all()
    return render(request, 'student_form.html', {'form': form, 'students': students})

def course_view(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_view')
    else:
        form = CourseForm()
    
    courses = Course.objects.all()
    return render(request, 'course_form.html', {'form': form, 'courses': courses})
