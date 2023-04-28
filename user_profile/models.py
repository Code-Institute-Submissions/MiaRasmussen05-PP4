from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    fiName = models.CharField(max_length=150, null=True, blank=True, default='')
    laName = models.CharField(max_length=150, null=True, blank=True, default='')
    email = models.CharField(max_length=250, null=True, blank=True, default='')
    birth_date = models.DateField(null=True, blank=True, default='')
    image = CloudinaryField('image', null=True, blank=True)
    bio = models.TextField(max_length=1000, null=True, blank=True, default='')

    def __str__(self):
        return f'{self.user.username} Profile'
