from django.urls import path
from .views import student_view, course_view
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('crud/', views.crud, name = "crud"),
    path('students/', student_view, name='student_view'),
    path('courses/', course_view, name='course_view')
]
