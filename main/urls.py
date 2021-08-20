from django.urls import path,include
from .views import index,AnnouncementDetailView,AnnouncementCreateView,AnnouncementUpdateView,AnnouncementDeleteView 

urlpatterns = [
    path('',index,name='main-home'),
    path('an/<int:pk>/',AnnouncementDetailView.as_view(),name='ancmnt-detail'),
    path('an/<int:pk>/update/',AnnouncementUpdateView.as_view(),name='ancmnt-update'),
    path('an/<int:pk>/delete/',AnnouncementDeleteView.as_view(),name='ancmnt-delete'),
    path('an/new/',AnnouncementCreateView.as_view(),name='ancmnt-create'),
]