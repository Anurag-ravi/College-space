from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Post,Like,Comment
from .forms import PostForm,CommentForm
from users.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    posts = Post.objects.all()
    profile = Profile.objects.get(user=request.user)
    p_form = PostForm()
    c_form = CommentForm()
    if 'p_submit' in request.POST:
        p_form = PostForm(request.POST,request.FILES)
        if p_form.is_valid():
            p_form.instance.author = request.user.profile
            p_form.save()
            messages.success(request,f'New Post Has Been Created')
            p_form = PostForm()
    if 'c_submit' in request.POST:
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            c_form.instance.user = request.user.profile
            c_form.instance.post = Post.objects.get(id=request.POST.get('post_id'))
            c_form.save()
            c_form = CommentForm()
    param = {
        'posts':posts,
        'title':'home',
        'profile':profile,
        'p_form': p_form,
        'c_form':c_form,
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

def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id = post_id)
        profile = Profile.objects.get(user = user)
        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like,created = Like.objects.get_or_create(user=profile,post_id = post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'
        post_obj.save()
        like.save()
    return redirect('connect-home')

class PostDeleteView(DeleteView,LoginRequiredMixin,UserPassesTestMixin):
    model = Post
    template_name = 'social/post_confirm_delete.html'
    success_url = reverse_lazy('connect-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user.profile == post.author:
            return True
        return False
    def get_object(self, *args,**kwargs):
        pk = self.kwargs.get('pk')
        obj = Post.objects.get(pk=pk)
        return obj

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'social/post_update.html'
    success_url = reverse_lazy('self-posts')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        if form.instance.author == profile:
            return super().form_valid(form)
        else:
            form.add_error(None, "You need to be post creator in order to update it")
            return super().form_invalid(form)

class CommentDeleteView(DeleteView,LoginRequiredMixin,UserPassesTestMixin):
    model = Comment
    template_name = 'social/comment_confirm_delete.html'
    success_url = reverse_lazy('connect-home')

    def test_func(self):
        comment = self.get_object()
        if self.request.user.profile == comment.user:
            return True
        return False
    def get_object(self, *args,**kwargs):
        pk = self.kwargs.get('pk')
        obj = Comment.objects.get(pk=pk)
        return obj

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'social/comment_update.html'
    success_url = reverse_lazy('connect-home')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        if form.instance.user == profile:
            return super().form_valid(form)
        else:
            form.add_error(None, "You need to be commentor in order to update it")
            return super().form_invalid(form)