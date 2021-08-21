from django.urls import path,include
from .views import index,self_posts,like_unlike_post
urlpatterns = [
    path('',index,name = 'connect-home'),
    path('selfpost/',self_posts,name = 'self-posts'),
    path('liked/',like_unlike_post,name = 'like_unlike'),
]