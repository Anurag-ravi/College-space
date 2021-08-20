# from __future__ import absolute_import,unicode_literals
# import os

# from celery import Celery
# from django.conf import settings
# from celery.schedules import crontab

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'college_space.settings')

# app = Celery('college_space')
# app.conf.enable_utc = False
# app.conf.update(timezone = 'Asia/Kolkata')

# app.config_from_object(settings,namespace='CELERY')

# # Celery Beat Settings
# app.conf.beat_schedule = {
#     # "send-mail-daily" : {
#     #     'task' : 'main.tasks.mailfunc',
#     #     'schedule' : crontab(hour = 12,minute=18),
#     # }
# }

# app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')


# #command
# # celery -A college_space.celery worker --pool=solo -l info
# # celery -A college_space beat -l INFO 