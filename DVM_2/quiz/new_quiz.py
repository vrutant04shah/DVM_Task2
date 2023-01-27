from django.contrib.auth.forms import UserCreationForm

from .models import Question
from django import forms


class Question_creation(UserCreationForm):
    question = forms.CharField(max_length=100)
    option1 = forms.CharField(max_length=50)
    option2 = forms.CharField(max_length=50)
    option3 = forms.CharField(max_length=50)
    option4 = forms.CharField(max_length=50)
    options = (
        ('A', f'{option1}'),
        ('B', f'{option2}'),
        ('C', f'{option3}'),
        ('D', f'{option4}')
    )
    answer = forms.ChoiceField(choices=options)

    class Meta:
        model = Question
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'answer']
