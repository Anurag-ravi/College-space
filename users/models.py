from django.db import models
from django.contrib.auth.models import User  # 200101017

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default='0')
    roll = models.CharField(max_length=9,default='0')
    batch = models.CharField(max_length=13,default='0')
    programme = models.CharField(max_length=13,default='0')
    department = models.CharField(max_length=50,default='0')
    br = models.BooleanField(default=False)
    section = models.CharField(max_length=1,default="0")
    friends = models.ManyToManyField(User,blank=True,related_name = 'friends')
    bio = models.TextField(default = "...",max_length = 300)
    avatar = models.ImageField(default ='/avatars/profile.jpg', upload_to='avatar/')

    def __str__(self):
        return f'{self.user.first_name} profile'

STATUS_CHOICES = (
    ('send','send'),
    ('accepted','accepted'),
)

class Relationship(models.Model):
    sender = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='sender')
    receiver = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='receiver')
    status = models.CharField(max_length=8,choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sender} -> {self.receiver} -> {self.status}'