from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Timetable,Monday,Thursday,Tuesday,Wednesday,Friday
from .forms import MondayUpdateForm,TuesdayUpdateForm,WednesdayUpdateForm,ThursdayUpdateForm,FridayUpdateForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
now = datetime.now().hour
if now < 12 and now >= 6:
    s = "Good Morning"
elif now >= 12 and now < 16:
    s = "Good Afternoon"
elif now >= 16 and now < 19:
    s = "Good Evening"
else:
    s = "Good Night"

@login_required
def timetable(request):
    param = {
        'tts': Timetable.objects.filter(batch = request.user.profile.batch, department = request.user.profile.department, section = request.user.profile.section),
        'str':s,
    }
    return render(request, 'timetable/timetable.html',param)

@login_required
def timetable_update(request):
    if request.user.profile.br:
        if request.method == 'POST':
            m_form=MondayUpdateForm(request.POST,request.FILES,instance=Monday.objects.filter(parent__batch = request.user.profile.batch, parent__department = request.user.profile.department, parent__section = request.user.profile.section).first())
            t_form=TuesdayUpdateForm(request.POST,request.FILES,instance=Tuesday.objects.filter(parent__batch = request.user.profile.batch, parent__department = request.user.profile.department, parent__section = request.user.profile.section).first())
            w_form=WednesdayUpdateForm(request.POST,request.FILES,instance=Wednesday.objects.filter(parent__batch = request.user.profile.batch, parent__department = request.user.profile.department, parent__section = request.user.profile.section).first())
            th_form=ThursdayUpdateForm(request.POST,request.FILES,instance=Thursday.objects.filter(parent__batch = request.user.profile.batch, parent__department = request.user.profile.department, parent__section = request.user.profile.section).first())
            f_form=FridayUpdateForm(request.POST,request.FILES,instance=Friday.objects.filter(parent__batch = request.user.profile.batch, parent__department = request.user.profile.department, parent__section = request.user.profile.section).first())
            if m_form.is_valid() and t_form.is_valid() and w_form.is_valid() and th_form.is_valid() and f_form.is_valid():
                m_form.save()
                t_form.save()
                w_form.save()
                th_form.save()
                f_form.save()
                messages.success(request,f'''Your Batch's Timetable has been updated!''')
                return redirect('timetable')
        else:
            m_form=MondayUpdateForm(instance=Monday.objects.filter(parent__batch = request.user.profile.batch, parent__department = request.user.profile.department, parent__section = request.user.profile.section).first())
            t_form=TuesdayUpdateForm(instance=Tuesday.objects.filter(parent__batch = request.user.profile.batch, parent__department = request.user.profile.department, parent__section = request.user.profile.section).first())
            w_form=WednesdayUpdateForm(instance=Wednesday.objects.filter(parent__batch = request.user.profile.batch, parent__department = request.user.profile.department, parent__section = request.user.profile.section).first())
            th_form=ThursdayUpdateForm(instance=Thursday.objects.filter(parent__batch = request.user.profile.batch, parent__department = request.user.profile.department, parent__section = request.user.profile.section).first())
            f_form=FridayUpdateForm(instance=Friday.objects.filter(parent__batch = request.user.profile.batch, parent__department = request.user.profile.department, parent__section = request.user.profile.section).first())
        return render(request, 'timetable/timetable_update.html',{'title':'timetable-update' , 'm_form':m_form , 't_form':t_form , 'w_form':w_form , 'th_form':th_form , 'f_form':f_form,'str':s})
    else:
        param = {
        'tts': Timetable.objects.filter(batch = request.user.profile.batch, department = request.user.profile.department, section = request.user.profile.section),
        'str':s,
        }
        return render(request, 'timetable/timetable.html',param)
