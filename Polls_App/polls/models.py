from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_text = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choices = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)