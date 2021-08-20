from django.urls import path
from .views import timetable_update, timetable

urlpatterns = [
    path('',timetable,name='timetable'),
    path('update/',timetable_update,name='timetable-update'),
]