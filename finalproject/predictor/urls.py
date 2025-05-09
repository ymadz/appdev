from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),               
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('predict/', views.predict_overall, name='predict'),
    path('logout/', views.logout_view, name='logout'),
]
