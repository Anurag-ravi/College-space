from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
# Create your views here.
def index(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        p_form = PostForm(request.POST,request.FILES)
        if p_form.is_valid():
            p_form.instance.author = request.user.profile
            p_form.save()
            messages.success(request,f'New Post Has Been Created')
            return redirect('connect-home')
    else:
        p_form = PostForm()
    param = {
        'posts':posts,
        'title':'',
        'p_form': p_form,
    }
    return render(request, 'social/index.html',param)

def self_posts(request):
    posts = Post.objects.filter(author = request.user.profile)
    if request.method == 'POST':
        p_form = PostForm(request.POST,request.FILES)
        if p_form.is_valid():
            p_form.instance.author = request.user.profile
            p_form.save()
            messages.success(request,f'New Post Has Been Created')
            return redirect('self-posts')
    else:
        p_form = PostForm()
    param = {
        'posts':posts,
        'title':'My Posts',
        'p_form': p_form,
    }
    return render(request, 'social/mypost.html',param)