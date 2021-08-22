from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import ProfileUpdateForm
from .models import Relationship,Profile
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import Q
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

def invite_received_view(request):
    profile = Profile.objects.get(user=request.user)
    qs = Relationship.objects.invitations_received(profile)
    result = list(map(lambda x: x.sender,qs))
    is_empty = False
    if len(result) == 0:
        is_empty=True
    param = {
        'qs':result,
        'is_empty':is_empty,
    }
    return render(request,'users/my_invites.html',param)
def accept_invitation(request):
    if request.method == 'POST':
        pk = request.POST.get('profile_pk')
        sender = Profile.objects.get(pk=pk)
        receiver = Profile.objects.get(user=request.user)
        rel = get_object_or_404(Relationship,sender=sender,receiver=receiver)
        if rel.status == 'send':
            rel.status = 'accepted'
            rel.save()
    return redirect('my-invites')


def reject_invitation(request):
    if request.method == 'POST':
        pk = request.POST.get('profile_pk')
        sender = Profile.objects.get(pk=pk)
        receiver = Profile.objects.get(user=request.user)
        rel = get_object_or_404(Relationship,sender=sender,receiver=receiver)
        rel.delete()
    return redirect('my-invites')
def invite_profile_list(request):
    user = request.user
    qs = Profile.objects.get_all_profile_to_invite(user)

    param = {
        'qs':qs
    }
    return render(request,'users/invite_list.html',param)

class ProfileListView(ListView):
    model = Profile
    template_name = 'users/profile_list.html'

    def get_queryset(self):
        qs = Profile.objects.get_all_profiles(self.request.user)
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        rel_r = Relationship.objects.filter(sender=profile)
        rel_s = Relationship.objects.filter(receiver=profile)
        rel_receiver = []
        rel_sender = []
        for item in rel_r:
            rel_receiver.append(item.receiver.user)
        for item in rel_s:
            rel_sender.append(item.sender.user)
        context["rel_receiver"]=rel_receiver
        context["rel_sender"]=rel_sender
        context["is_empty"] = False
        if len(self.get_queryset()) == 0:
            context["is_empty"] = True

        return context

def send_invitation(request):
    if request.method == 'POST':
        pk = request.POST.get('profile_pk')
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        rel = Relationship.objects.create(sender=sender,receiver=receiver,status='send')

        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profile-list')

def remove_friend(request):
    if request.method == 'POST':
        pk = request.POST.get('profile_pk')
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        rel = Relationship.objects.get((Q(sender=sender) & Q(receiver=receiver)) | (Q(sender=receiver) & Q(receiver=sender)))
        rel.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profile-list')