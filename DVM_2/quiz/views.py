from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Quiz, Question, Answer_Score
from .forms import New_Quiz, Question_Form


def home(request):
    return render(request, 'quiz/home.html')


class PostListView(ListView):
    model = Quiz
    template_name = 'quiz/home.html'
    context_object_name = 'quizzes'


class PostDetailView(DetailView):
    model = Quiz


@login_required
def create_quiz(request):
    if request.method == 'POST':
        form = New_Quiz(request.POST)
        if form.is_valid():
            new_quiz = form.save(commit=False)
            new_quiz.author = request.user
            new_quiz.save()
            return redirect('newquiz-detail', pk=new_quiz.pk)
    else:
        form = New_Quiz()
    return render(request, 'quiz/create_quiz.html', {'form': form})


@login_required
def add_question(request):
    if request.method == 'POST':
        form = Question_Form(request.POST)
        if form.is_valid():
            return redirect('question-detail')
    else:
        form = Question_Form
    return render(request, 'quiz/create_quiz.html', {'form': form})


@login_required
def quiz_detail(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = quiz.question_set.all()
    return render(request, 'quiz/question_detail.html', {'questions': questions, 'pk': pk, 'quiz': quiz})
