from django.test import TestCase
from django.urls import resolve, reverse
from blog.views import (
    home, ShopView, ShopCategoryView, ShopItemView, AddShopItemView,
    EditShopItem, DeleteShopItem, EditReview, DeleteReview, BlogList,
    BlogDetail, BlogLike, AddBlogView, EditBlog, DeleteBlog, EditCommentView,
    DeleteCommentView, ProjectList, AddProjectView, EditProject, DeleteProject,
    GalleryView, AddImageView, EditGallery, DeleteGallery, contact
)
from blog.models import (
    ShopCategory, Shop, Review, Blog, Comment, Projects, Images)


class TestUrls(TestCase):

    def test_home_url(self):
        """Tests Index URL"""
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_ShopView_url(self):
        """Tests Shop Page URL"""
        url = reverse('shop')
        self.assertEquals(resolve(url).func.view_class, ShopView)

    def test_ShopCategoryView_url(self):
        """Tests Shop Categories URL"""
        url = reverse('shop_category', kwargs={'shop_category_id': 1})
        self.assertEquals(resolve(url).func.view_class, ShopCategoryView)

    def test_ShopItemView_url(self):
        """Tests Shop Items Page URL"""
        url = reverse('shop_item', kwargs={'shop_id': 1})
        self.assertEquals(resolve(url).func.view_class, ShopItemView)

    def test_AddShopItemView_url(self):
        """Tests Add Shop Items URL"""
        url = reverse('add_product')
        self.assertEquals(resolve(url).func.view_class, AddShopItemView)

    def test_EditShopItem_url(self):
        """Tests Edit Shop Item URL"""
        url = reverse('edit_shop', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, EditShopItem)

    def test_DeleteShopItem_url(self):
        """Tests Delete Shop Item URL"""
        url = reverse('delete_shop', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, DeleteShopItem)

    def test_EditReview_url(self):
        """Tests Edit Review URL"""
        url = reverse('edit-review', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, EditReview)

    def test_DeleteReview_url(self):
        """Tests Delete Review URL"""
        url = reverse('delete-review', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, DeleteReview)

    def test_BlogList_url(self):
        """Tests Blog Page URL"""
        url = reverse('blog')
        self.assertEquals(resolve(url).func.view_class, BlogList)

    def test_BlogList_post_url(self):
        """Tests Blog List URL"""
        url = reverse('blog_list')
        self.assertEquals(resolve(url).func.view_class, BlogList)

    def test_BlogDetail_url(self):
        """Tests Blog Post Page URL"""
        url = reverse('blog_post', kwargs={'slug': 1})
        self.assertEquals(resolve(url).func.view_class, BlogDetail)

    def test_BlogLike_url(self):
        """Tests Blog Likes URL"""
        url = reverse('blog_like', kwargs={'slug': 1})
        self.assertEquals(resolve(url).func.view_class, BlogLike)

    def test_AddBlogView_url(self):
        """Tests Add Blog URL"""
        url = reverse('add_blog')
        self.assertEquals(resolve(url).func.view_class, AddBlogView)

    def test_EditBlog_url(self):
        """Tests Edit Blog URL"""
        url = reverse('edit_blog', kwargs={'slug': 1})
        self.assertEquals(resolve(url).func.view_class, EditBlog)

    def test_DeleteBlog_url(self):
        """Tests Delete Blog URL"""
        url = reverse('delete_blog', kwargs={'slug': 1})
        self.assertEquals(resolve(url).func.view_class, DeleteBlog)

    def test_EditCommentView_url(self):
        """Tests Edit Comment URL"""
        url = reverse('edit-comment', kwargs={'comment_id': 1})
        self.assertEquals(resolve(url).func.view_class, EditCommentView)

    def test_DeleteCommentView_url(self):
        """Tests Delete Comment URL"""
        url = reverse('delete-comment', kwargs={'comment_id': 1})
        self.assertEquals(resolve(url).func.view_class, DeleteCommentView)

    def test_ProjectList_url(self):
        """Tests Portfolio Page URL"""
        url = reverse('portfolio')
        self.assertEquals(resolve(url).func.view_class, ProjectList)

    def test_AddProjectView_url(self):
        """Tests Add Portfolio Project URL"""
        url = reverse('add_project')
        self.assertEquals(resolve(url).func.view_class, AddProjectView)

    def test_EditProject_url(self):
        """Tests Edit Portfolio Project URL"""
        url = reverse('edit_project', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, EditProject)

    def test_DeleteProject_url(self):
        """Tests Delete Portfolio Project URL"""
        url = reverse('delete_project', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, DeleteProject)

    def test_GalleryView_url(self):
        """Tests Gallery Page URL"""
        url = reverse('gallery')
        self.assertEquals(resolve(url).func.view_class, GalleryView)

    def test_GalleryView_category_url(self):
        """Tests Gallery Page Categories URL"""
        url = reverse('gallery_category', kwargs={'category_id': 1})
        self.assertEquals(resolve(url).func.view_class, GalleryView)

    def test_AddImageView_url(self):
        """Tests Add Image URL"""
        url = reverse('add_image')
        self.assertEquals(resolve(url).func.view_class, AddImageView)

    def test_EditGallery_url(self):
        """Tests Edit Image URL"""
        url = reverse('edit_image', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, EditGallery)

    def test_DeleteGallery_url(self):
        """Tests Delete Image URL"""
        url = reverse('delete_image', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, DeleteGallery)

    def test_contact_url(self):
        """Tests Contact Page URL"""
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)
