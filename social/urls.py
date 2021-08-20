from django.urls import path,include
from .views import index,self_posts
urlpatterns = [
    path('',index,name = 'connect-home'),
    path('selfpost/',self_posts,name = 'self-posts'),
]