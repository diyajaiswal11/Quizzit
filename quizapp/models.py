from django.db import models

# Create your models here.


class Question(models.Model):
    question=models.CharField(max_length=100)

    def __str__(self):
        return self.question




class Answer(models.Model):
    que=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer=models.CharField(max_length=100) 

    def __str__(self):
        return self.answer


