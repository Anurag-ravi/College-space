from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    return render(request, 'social/basic.html')

def self_posts(request):
    posts = Post.objects.filter(author = request.user.profile)
    param = {
        'posts':posts,
        'title':'My Posts'
    }
    return render(request, 'social/mypost.html',param)