from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Authors CRUD
    path('authors/', views.author_list, name='author_list'),
    path('authors/save/', views.author_save, name='author_save'),
    path('authors/edit/<int:pk>/', views.author_edit, name='author_edit'),
    path('authors/delete/<int:pk>/', views.author_delete, name='author_delete'),

    # Books CRUD
    path('books/', views.book_list, name='book_list'),
    path('books/save/', views.book_save, name='book_save'),
    path('books/edit/<int:pk>/', views.book_edit, name='book_edit'),
    path('books/delete/<int:pk>/', views.book_delete, name='book_delete'),
]
