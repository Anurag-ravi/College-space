from django.urls import include, path, reverse
from .views import index,self_posts,like_unlike_post,PostDeleteView,PostUpdateView,CommentDeleteView,CommentUpdateView
urlpatterns = [
    path('',index,name = 'connect-home'),
    path('selfpost/',self_posts,name = 'self-posts'),
    path('liked/',like_unlike_post,name = 'like_unlike'),
    path('<pk>/delete/',PostDeleteView.as_view(),name = 'post-delete'),
    path('<pk>/update/',PostUpdateView.as_view(),name = 'post-update'),
    path('c/<pk>/delete/',CommentDeleteView.as_view(),name = 'com-delete'),
    path('c/<pk>/update/',CommentUpdateView.as_view(),name = 'com-update'),
]