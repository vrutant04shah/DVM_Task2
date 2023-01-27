from django import forms
from .models import Question, Quiz


class New_Quiz(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title']

    def save(self, commit=True):
        quiz = super().save(commit=False)
        if commit:
            quiz.save()
        return quiz


class Question_Form(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'answer']

    def save(self, commit=True):
        question = super().save(commit=False)
        if commit:
            question.save()
        return question
