from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('发布日期')
    #objects = models.Manager()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 定义外键关系，
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
