from django.urls import path
from users import views as user_views

urlpatterns = [
    path('',user_views.profile, name='profile'),
    path('profile_list/',user_views.ProfileListView.as_view(), name='profile-list'),
    path('invite_list/',user_views.invite_profile_list, name='invite-list'),
    path('my_invites/',user_views.invite_received_view, name='my-invites'),
    path('send_invite/',user_views.send_invitation, name='send-invites'),
    path('remove_friend/',user_views.remove_friend, name='remove-friend'),
    path('my_invites/accept/',user_views.accept_invitation, name='accept-invite'),
    path('my_invites/reject/',user_views.reject_invitation, name='reject-invite'),
]