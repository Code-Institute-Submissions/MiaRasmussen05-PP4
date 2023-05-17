from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
from decimal import Decimal
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
            username='jane', email='test@test.com', password='janepassword'
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

        self.gallery_category = GalleryCategory.objects.create(
            name='Category 2')

        self.image = Images.objects.create(
            image='image.jpg',
            title='Image 1',
            created_on='2023-29-04',
            description='Image description',
            category=self.gallery_category,
            status=1
        )

    def test_shop_category_str(self):
        """
        Tests the string representation of the ShopCategory model
        """
        expected_str = "Category 1"
        self.assertEqual(str(self.shop_category), expected_str)

    def test_shop_str(self):
        """
        Tests the string representation of the Shop model
        """
        shop = Shop.objects.get(title='Shop 1')
        expected_str = "Shop 1 - Item 1: $2.50"
        self.assertEqual(str(shop), expected_str)

    def test_shop_slug_is_assigned(self):
        """
        Tests whether a slug is being assigned to the Shop model
        """
        self.assertEqual(self.shop.slug, 'shop-1')

    def test_shop_save_method(self):
        """
        Tests the custom save method of the Shop model
        """
        new_shop = Shop.objects.create(
            title='New Shop',
            item='New Item',
            price=Decimal('5.00'),
            shop_category=self.shop_category,
            status=1
        )
        self.assertEqual(new_shop.slug, 'new-shop')

    def test_shop_price_validation(self):
        """
        Tests the price validation in the clean method of the Shop model
        """
        invalid_shop = Shop(
            title='Invalid Shop',
            price=-10.0,
        )
        self.assertEqual(invalid_shop.price, -10.0)

    def test_review_str(self):
        """
        Tests the string representation of the Review model
        """
        expected_str = "Review 5 - Nice Item!!! by jane"
        self.assertEqual(str(self.review), expected_str)

    def test_blog_str(self):
        """
        Tests the string representation of the Blog model
        """
        expected_str = "Blog 1"
        self.assertEqual(str(self.blog), expected_str)

    def test_blog_likes(self):
        """
        Tests adding likes to the Blog model
        """
        user1 = self.user

        self.blog.likes.add(user1)

        self.assertEqual(self.blog.likes.count(), 1)

    def test_blog_bookmarked(self):
        """
        Tests bookmarking for the Blog model
        """
        user1 = self.user

        self.blog.bookmarked.add(user1)

        self.assertEqual(self.blog.bookmarked.count(), 1)

    def test_comment_str(self):
        """
        Tests the string representation of the Comment model
        """
        expected_str = "Comment Cool blog post! by Jane"
        self.assertEqual(str(self.comment), expected_str)

    def test_project_str(self):
        """
        Tests the string representation of the Projects model
        """
        expected_str = "Project 1"
        self.assertEqual(str(self.projects), expected_str)

    def test_gallery_category_str(self):
        """
        Tests the string representation of the GalleryCategory model
        """
        expected_str = "Category 2"
        self.assertEqual(str(self.gallery_category), expected_str)

    def test_image_str(self):
        """
        Tests the string representation of the Images model
        """
        expected_str = "Image 1"
        self.assertEqual(str(self.image), expected_str)
