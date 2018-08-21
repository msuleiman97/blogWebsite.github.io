
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(blank=True)
    phone = models.IntegerField(blank=True)
    image = models.ImageField(upload_to='profile_image', default='../style/profile.jpg')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default="")
    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)