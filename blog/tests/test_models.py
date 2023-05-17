from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from blog.models import (
    ShopCategory, Shop, Review, Blog, Comment, Projects, Images)
from blog.views import GalleryCategory


class TestModels(TestCase):
    """
    Sets up the user and models for the tests
    """
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='mia', email='test@test.com', password='miapassword'
        )

        self.shop_category = ShopCategory.objects.create(name='Category 1')

        self.shop = Shop.objects.create(
            title='Shop 1',
            slug=slugify('Shop 1'),
            item='Item 1',
            price=2.50,
            shop_category=self.shop_category,
            status=1
        )

        self.review = Review.objects.create(
            comment=self.shop,
            user=self.user,
            name='Jane',
            email='jane@example.com',
            text='Nice Item!!!',
            rating=5
        )

        self.blog = Blog.objects.create(
            title='Blog 1',
            slug=slugify('Blog 1'),
            content='Lorem ipsum dolor sit amet.',
            status=1
        )

        self.comment = Comment.objects.create(
            post=self.blog,
            user=self.user,
            name='Jane',
            email='jane@example.com',
            body='Cool blog post!'
        )

        self.projects = Projects.objects.create(
            title='Project 1',
            image='image1.jpg',
            created_on='2023-29-04',
            description='Project description.',
            status=1
        )

        self.gallery_category = GalleryCategory.objects.create(name='Category 1')

        self.image = Images.objects.create(
            image='image.jpg',
            title='Image 1',
            created_on='2023-29-04',
            description='Image description',
            category=self.gallery_category,
            status=1
        )
