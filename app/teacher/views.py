from django.views.generic import TemplateView, DetailView, FormView
from .models import Question, Student
from .forms import QuestionForm
from django.contrib import messages

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Student.objects.all()
        return context


class QuestionsView(TemplateView):
    template_name = "questions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["questions"] = Question.objects.all()
        return context


class QuestionDetailView(DetailView):
    template_name = "question_detail.html"
    model = Question


class AddQuestionView(FormView):
    template_name = "add_question.html"
    form_class = QuestionForm
    success_url = "/questions"

    def form_valid(self, form):
        print(form.cleaned_data['text'])
        Question.objects.create(
            text=form.cleaned_data['text'],
            image=form.cleaned_data['image']
        )
        messages.info(self.request, "Question added")
        return super().form_valid(form)
