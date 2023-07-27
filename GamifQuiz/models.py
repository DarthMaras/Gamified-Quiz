from tkinter.messagebox import QUESTION
from django.db import models
from django.contrib.auth.models import User


#models for  questions and answers 
class Quiz(models.Model):
    username = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
class Meta:
    app_label = 'GamifQuiz'

    # i guess this is the username 
    def __str__(self):
        return self.username

class Question(models.Model):
    question_text = models.CharField(max_length=200)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    extra_information = models.TextField()

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    points_awarded = models.IntegerField(default=0)

class Badge(models.Model):
    badge_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='badges/')

class UserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)

class Reward(models.Model):
    reward_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='rewards/')

class UserReward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    insightful = models.BooleanField()
    happy = models.BooleanField()
    motivational = models.BooleanField()
    thoughts = models.TextField()

