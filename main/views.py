from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from timetable import models
from datetime import datetime,date
from quiz.models import Quiz,Assignment
from .models import Announcement
from timetable.models import Timetable,Monday,Tuesday,Wednesday,Thursday,Friday
import calendar
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import AnnouncementForm



curr_date = date.today()
day = calendar.day_name[curr_date.weekday()]
now = datetime.now().hour
if now < 12 and now >= 6:
    s = "Good Morning"
elif now >= 12 and now < 16:
    s = "Good Afternoon"
elif now >= 16 and now < 19 :
    s = "Good Evening"
else:
    s = "Good Night"

daymap = {
    'Monday': Monday,
    'Tuesday': Tuesday,
    'Wednesday': Wednesday,
    'Thursday': Thursday,
    'Friday': Friday,
}
@login_required
def index(request):
    quiz_count = Quiz.objects.filter(batch = request.user.profile.batch, department = request.user.profile.department, section = request.user.profile.section).count()
    asgn_count = Assignment.objects.filter(batch = request.user.profile.batch, department = request.user.profile.department, section = request.user.profile.section).count()
    announcemnts = Announcement.objects.filter(batch = request.user.profile.batch, department = request.user.profile.department, section = request.user.profile.section)
    
    try :
        today = daymap[day].objects.filter(parent__batch = request.user.profile.batch, parent__department = request.user.profile.department, parent__section = request.user.profile.section,).first()
        class_count=0
        if (today.eight_nine)!="-":
            class_count = class_count + 1
        if (today.nine_ten)!="-":
            class_count = class_count + 1
        if (today.ten_eleven)!="-":
            class_count = class_count + 1
        if (today.eleven_twelve)!="-":
            class_count = class_count + 1
        if (today.twelve_one)!="-":
            class_count = class_count + 1
        if (today.two_three)!="-":
            class_count = class_count + 1
        if (today.three_four)!="-":
            class_count = class_count + 1
        if (today.four_five)!="-":
            class_count = class_count + 1
        if (today.five_six)!="-":
            class_count = class_count + 1
    except:
        class_count = 0

    param = {
        'title': 'Dashboard',
        'str':s,
        'quiz_count':quiz_count,
        'asgn_count':asgn_count,
        'class_count':class_count,
        'announcements':announcemnts
    }
    return render(request, 'main/index.html',param)

# <===== Announcement Views =====>
class AnnouncementDetailView(LoginRequiredMixin, DetailView):
    model = Announcement

class AnnouncementCreateView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Announcement
    form_class = AnnouncementForm
    def form_valid(self, form):
        form.instance.batch = self.request.user.profile.batch
        form.instance.department = self.request.user.profile.department
        form.instance.section = self.request.user.profile.section
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.profile.br:
            return True
        return False

class AnnouncementUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Announcement
    form_class = AnnouncementForm
    def form_valid(self, form):
        form.instance.batch = self.request.user.profile.batch
        form.instance.department = self.request.user.profile.department
        form.instance.section = self.request.user.profile.section
        return super().form_valid(form)
    
    def test_func(self):
        announcement = self.get_object()
        if self.request.user.profile.batch == announcement.batch and self.request.user.profile.department == announcement.department and self.request.user.profile.section == announcement.section and self.request.user.profile.br:
            return True
        return False

class AnnouncementDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Announcement
    success_url = '/'

    def test_func(self):
        announcement = self.get_object()
        if self.request.user.profile.batch == announcement.batch and self.request.user.profile.department == announcement.department and self.request.user.profile.section == announcement.section and self.request.user.profile.br:
            return True
        return False