from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    title = models.CharField(max_length=200, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=200, default=None)
    option1 = models.CharField(max_length=50, default=None)
    option2 = models.CharField(max_length=50, default=None)
    option3 = models.CharField(max_length=50, default=None)
    option4 = models.CharField(max_length=50, default=None)
    Choices = [
        ('A', 'option1'),
        ('B', 'option2'),
        ('C', 'option3'),
        ('D', 'option4'),
    ]
    answer = models.CharField(max_length=1, choices=Choices, default=None)

    def save(self, **kwargs):
        super().save()


class Answer_Score:
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(User, on_delete=models.CASCADE)