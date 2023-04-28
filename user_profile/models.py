from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fiName = models.CharField(max_length=150, null=True, blank=True)
    laName = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
