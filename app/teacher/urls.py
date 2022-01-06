from django.urls import path
from .views import \
    AddQuestionView, \
    HomePageView, \
    QuestionsView, \
    QuestionDetailView

app_name = 'teacher'

urlpatterns = [
    path('',
         HomePageView.as_view(), name='index'),
    path('questions',
         QuestionsView.as_view(), name='questions'),
    path('questions/<int:pk>/',
         QuestionDetailView.as_view(), name='question_detail'),
    path('questions/add/',
         AddQuestionView.as_view(), name='add_question')
]
