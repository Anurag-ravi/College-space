from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
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
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request,f'Your Profile Has Been Updated')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance = request.user.profile)
    param = {
        'title' : 'profile',
        'str' : s,
        'p_form' : p_form,
    }
    return render(request, 'users/profile.html',param)