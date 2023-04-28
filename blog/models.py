from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinLengthValidator
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))


class ShopCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Shop(models.Model):

    title = models.CharField(max_length=250, validators=[MinLengthValidator(4)], unique=True)
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=250, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    item = models.CharField(max_length=150, validators=[MinLengthValidator(4)])
    image = CloudinaryField('image', null=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    shop_category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE, related_name='shop', null=True, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    saved = models.ManyToManyField(User, related_name='save_shop', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title) + " - " + str(self.item) + ": $" + str(self.price)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def clean(self):
        if self.price is not None and self.price <= 0:
            raise ValidationError("The price can not go into the negative, hit zero or be blank")


class Review(models.Model):

    comment = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=False)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    text = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(choices=((0, '0 stars'), (1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')))

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.rating} - {self.text} by {self.user.username}"
