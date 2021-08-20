from django.contrib import admin
from .models import Timetable, Monday, Tuesday, Wednesday, Thursday, Friday

admin.site.register(Timetable)
admin.site.register(Monday)
admin.site.register(Tuesday)
admin.site.register(Wednesday)
admin.site.register(Thursday)
admin.site.register(Friday)