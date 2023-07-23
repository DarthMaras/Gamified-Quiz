# my_quiz_project/myquiz/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('quiz/', views.quiz, name='quiz'),
    
]
