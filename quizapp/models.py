from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Level(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    level=models.CharField(max_length=500,default=1) 
    score=models.CharField(max_length=2500,default=0)

    def __str__(self):
        return self.score



class Question(models.Model):
    question=models.CharField(max_length=100)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer=models.CharField(max_length=100,default='')


    def __str__(self):
        return self.answer


