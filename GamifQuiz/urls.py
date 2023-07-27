from django.urls import path
from GamifQuiz import views

app_name = 'GamifQuiz'

urlpatterns = [
    path('', views.start_quiz, name='start_quiz'),
    path('quiz/<int:question_number>/', views.quiz_question, name='quiz_question'), 
    path('result/', views.quiz_result, name='quiz_result'),
    path('feedback/', views.submit_feedback, name='submit_feedback'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('play-again', views.play_again, name='play_again')
]

