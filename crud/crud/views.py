from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm

# Create Student
def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save to database
            return redirect("student_list")  # Redirect to list view
    else:
        form = StudentForm()
    
    return render(request, "student_form.html", {"form": form, "title": "Add Student"})

def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)  # Load form with existing data
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)
    
    return render(request, "student_form.html", {"form": form, "title": "Edit Student"})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    
    return render(request, "delete_student.html", {"student": student})

# Create Course
def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm()
    
    return render(request, "course_form.html", {"form": form, "title": "Add Course"})

# List Courses
def course_list(request):
    courses = Course.objects.all()
    return render(request, "course_list.html", {"courses": courses})

# Update Course
def update_course(request, id):
    course = get_object_or_404(Course, id=id)
    
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm(instance=course)
    
    return render(request, "course_form.html", {"form": form, "title": "Edit Course"})

# Delete Course
def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == "POST":
        course.delete()
        return redirect("course_list")
    
    return render(request, "delete_course.html", {"course": course})
