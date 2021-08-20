from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Quiz,Assignment
from datetime import datetime
from .forms import QuizForm,AssignmentForm


now = datetime.now().hour
if now < 12 and now >= 6:
    s = "Good Morning"
elif now >= 12 and now < 16:
    s = "Good Afternoon"
elif now >= 16 and now < 19:
    s = "Good Evening"
else:
    s = "Good Night"

# <===== Assignment Views =====>
def quizlist(request):
    quizs = Quiz.objects.filter(batch = request.user.profile.batch, department = request.user.profile.department, section = request.user.profile.section)
    assignments = Assignment.objects.filter(batch = request.user.profile.batch, department = request.user.profile.department, section = request.user.profile.section)
    # quizs = Quiz.objects.all()
    # assignments = Assignment.objects.all()
    param ={
        'title':'Q/A',
        'quizs':quizs,
        'assignments':assignments,
        'str':s,
    }
    return render(request, 'quiz/quiz_list.html',param)

class QuizDetailView(LoginRequiredMixin, DetailView):
    model = Quiz

class QuizCreateView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Quiz
    form_class = QuizForm
    def form_valid(self, form):
        form.instance.batch = self.request.user.profile.batch
        form.instance.department = self.request.user.profile.department
        form.instance.section = self.request.user.profile.section
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.profile.br:
            return True
        return False

class QuizUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Quiz
    form_class = QuizForm
    def form_valid(self, form):
        form.instance.batch = self.request.user.profile.batch
        form.instance.department = self.request.user.profile.department
        form.instance.section = self.request.user.profile.section
        return super().form_valid(form)
    
    def test_func(self):
        quiz = self.get_object()
        if self.request.user.profile.batch == quiz.batch and self.request.user.profile.department == quiz.department and self.request.user.profile.section == quiz.section and self.request.user.profile.br:
            return True
        return False

class QuizDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Quiz
    success_url = '/'

    def test_func(self):
        quiz = self.get_object()
        if self.request.user.profile.batch == quiz.batch and self.request.user.profile.department == quiz.department and self.request.user.profile.section == quiz.section and self.request.user.profile.br:
            return True
        return False

# <===== Assignment Views =====>
class AssignmentDetailView(LoginRequiredMixin, DetailView):
    model = Assignment

class AssignmentCreateView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Assignment
    form_class = AssignmentForm
    def form_valid(self, form):
        form.instance.batch = self.request.user.profile.batch
        form.instance.department = self.request.user.profile.department
        form.instance.section = self.request.user.profile.section
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.profile.br:
            return True
        return False

class AssignmentUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Assignment
    form_class = AssignmentForm
    def form_valid(self, form):
        form.instance.batch = self.request.user.profile.batch
        form.instance.department = self.request.user.profile.department
        form.instance.section = self.request.user.profile.section
        return super().form_valid(form)
    
    def test_func(self):
        assignment = self.get_object()
        if self.request.user.profile.batch == assignment.batch and self.request.user.profile.department == assignment.department and self.request.user.profile.section == assignment.section and self.request.user.profile.br:
            return True
        return False

class AssignmentDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Assignment
    success_url = '/'

    def test_func(self):
        assignment = self.get_object()
        if self.request.user.profile.batch == assignment.batch and self.request.user.profile.department == assignment.department and self.request.user.profile.section == assignment.section and self.request.user.profile.br:
            return True
        return False