from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_player_performance, name='predict_performance'),
]
