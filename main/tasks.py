# from celery import shared_task
# from django.core.mail import send_mail
# from quiz.models import Quiz,Assignment
# from college_space import settings
# from users.models import Profile
# from django.contrib.auth.models import User

# @shared_task(bind=True)
# def mailfunc(self):
#     mail_subject = "Testing"
#     message = "hello from college space" 
#     to_email = "kiranpragya2003@gmail.com"
#     send_mail(
#         subject = mail_subject,
#         message = message,
#         from_email = settings.EMAIL_HOST_USER,
#         recipient_list = [to_email],
#         fail_silently = True
#     )
#     return "done"

