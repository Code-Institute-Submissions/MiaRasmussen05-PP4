from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

from blog.models import Shop

import uuid


STATUS = ((0, "Pending"), (1, "Processing"), (2, "Shipped"), (3, "Delivered"),)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    fiName = models.CharField(max_length=150, null=True, blank=True, default='')
    laName = models.CharField(max_length=150, null=True, blank=True, default='')
    email = models.CharField(max_length=250, null=True, blank=True, default='')
    image = CloudinaryField('image', null=True, blank=True)
    bio = models.TextField(max_length=1000, null=True, blank=True, default=None)
    orders = models.ManyToManyField('Order', blank=True, related_name='profile_orders')

    def __str__(self):
        return f'{self.user.username} Profile'


class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='information')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    order_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"{self.user.username}'s order for {self.quantity} x {self.item.title}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.item.title} for order {self.order.id}"
