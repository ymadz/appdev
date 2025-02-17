from django.urls import path
from .views import (
    create_student, student_list, update_student, delete_student,
    create_course, course_list, update_course, delete_course
)

urlpatterns = [
    # Student URLs
    path("students/", student_list, name="student_list"),
    path("students/create/", create_student, name="create_student"),
    path("students/update/<int:id>/", update_student, name="update_student"),
    path("students/delete/<int:id>/", delete_student, name="delete_student"),

    # Course URLs
    path("courses/", course_list, name="course_list"),
    path("courses/create/", create_course, name="create_course"),
    path("courses/update/<int:id>/", update_course, name="update_course"),
    path("courses/delete/<int:id>/", delete_course, name="delete_course"),
]
