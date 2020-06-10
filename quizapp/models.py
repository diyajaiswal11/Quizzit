from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Level(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    level=models.IntegerField(default=6) 
    score=models.IntegerField(default=0)

    def __str__(self):
        return self.user.username 
    



class Question(models.Model):
    question=models.CharField(max_length=100)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer=models.CharField(max_length=100,default='')


    def __str__(self):
        return self.answer


