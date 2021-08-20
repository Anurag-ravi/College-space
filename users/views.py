from django.shortcuts import render,redirect
from django.contrib import messages
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
def profile(request):
    return render(request, 'users/profile.html',{'title':'profile','str':s})