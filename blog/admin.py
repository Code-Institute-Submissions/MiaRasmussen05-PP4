from django.contrib import admin
from .models import ShopCategory, Shop, Review, Blog, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ShopCategory)
class ShopCategoryAdmin(SummernoteModelAdmin):

    search_fields = ['name']


@admin.register(Shop)
class ShopAdmin(SummernoteModelAdmin):

    list_filter = ('status', 'created_on', 'item', 'price')
    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'description', 'price', 'item']
    summernote_fields = ('description')


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    list_filter = ('created_on', 'text', 'comment', 'user', 'rating')
    list_display = ('user', 'rating', 'text', 'comment', 'created_on')
    search_fields = ['user', 'rating', 'text']


@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):

    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on')
    search_fields = ('name', 'email', 'body')