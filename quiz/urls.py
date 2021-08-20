from django.urls import path
from .views import QuizDetailView,QuizCreateView,QuizUpdateView,QuizDeleteView
from .views import AssignmentDetailView,AssignmentCreateView,AssignmentUpdateView,AssignmentDeleteView
from .views import quizlist

urlpatterns = [
    path('',quizlist,name='quiz-home'),
    path('<int:pk>/',QuizDetailView.as_view(),name='quiz-detail'),
    path('<int:pk>/update/',QuizUpdateView.as_view(),name='quiz-update'),
    path('<int:pk>/delete/',QuizDeleteView.as_view(),name='quiz-delete'),
    path('new/',QuizCreateView.as_view(),name='quiz-create'),
    # path('a/',AssignmentListView.as_view(),name='asgn-home'),
    path('a/<int:pk>/',AssignmentDetailView.as_view(),name='asgn-detail'),
    path('a/<int:pk>/update/',AssignmentUpdateView.as_view(),name='asgn-update'),
    path('a/<int:pk>/delete/',AssignmentDeleteView.as_view(),name='asgn-delete'),
    path('a/new/',AssignmentCreateView.as_view(),name='asgn-create'),
]