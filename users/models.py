from django.db import models
from django.contrib.auth.models import User  # 200101017
from PIL import Image
from django.db.models import Q

class ProfileManager(models.Manager):
    def get_all_profiles(self, me):
        profiles = Profile.objects.all().exclude(user=me)
        return profiles

    def get_all_profile_to_invite(self,sender):
        profiles = Profile.objects.all().exclude(user=sender)
        profile = Profile.objects.get(user=sender)
        qs = Relationship.objects.filter(Q(sender=profile) | Q(receiver=profile))

        accepted = set([])
        for rel in qs:
            if rel.status == 'accepted':
                accepted.add(rel.receiver)
                accepted.add(rel.sender)
        available = [profile for profile in profiles if profile not in accepted]
        return available


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
    avatar = models.ImageField(default ='/avatars/profile.jpg', upload_to='avatars/')
    
    objects = ProfileManager()
    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()

    def get_post_no(self):
        return self.posts.all().count()

    def get_all_post(self):
        return self.posts.all()

    def get_all_likes_no(self):
        likes = self.like_set.all()
        total = 0
        for like in likes:
            if like.value == 'Like':
                total += 1
        return total

    def __str__(self):
        return f'{self.user.first_name} profile'

    def save(self):
        super().save()
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            size = (300,300)
            img.thumbnail(size)
            img.save(self.avatar.path)

STATUS_CHOICES = (
    ('send','send'),
    ('accepted','accepted'),
)
class RelationshipManager(models.Manager):
    def invitations_received(self,receiver):
        qs = Relationship.objects.filter(receiver = receiver,status='send')
        return qs


class Relationship(models.Model):
    sender = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='sender')
    receiver = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='receiver')
    status = models.CharField(max_length=8,choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now=True)
    
    objects = RelationshipManager()
    def __str__(self):
        return f'{self.sender} -> {self.receiver} -> {self.status}'