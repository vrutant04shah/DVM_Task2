from django.urls import path
from .views import PostListView, PostDetailView, add_question, create_quiz, quiz_detail

urlpatterns = [
    path('', PostListView.as_view(), name='quiz-home'),
    path('quiz/<int:pk>/', PostDetailView.as_view(), name="quiz-detail"),
    path('quiz/new/', create_quiz, name="new-quiz"),
    path('quiz/new/add_question/', add_question, name="add-question"),
    path('quiz/new/quiz_detail/', quiz_detail, name="newquiz-detail")
]
