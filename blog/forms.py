from .models import Review, Comment, Shop, GalleryCategory, Images, Projects, Blog
from django import forms
from django.forms.widgets import ClearableFileInput


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'text',)
        widgets = {
            'rating': forms.NumberInput(attrs={
                'placeholder': 'Give your rating here 0-5...',
                'min': 0, 'max': 5, 'step': 1,
                'style': 'padding: 4px; display: block;'
            }),
            'text': forms.Textarea(attrs={
                'placeholder': 'Share your thoughts...',
                'rows': 5, 'maxlength': '1000',
                'style': 'padding: 10px; max-height: 200px; width: 100%;'
            }),
        }
        labels = {
            'rating': 'Stars:',
            'text': 'Review:',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': 'Share your thoughts...',
                'rows': 5, 'maxlength': '1000',
                'style': 'padding: 10px; max-height: 200px; width: 100%;'
            }),
        }
        labels = {
            'body': ''
        }


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('title', 'item', 'image', 'description', 'price', 'shop_category', 'status')
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title...',
                'style': 'padding: 4px; width: 100%;'
            }),
            'item': forms.TextInput(attrs={
                'placeholder': 'Item...',
                'style': 'padding: 4px; width: 100%;'
            }),
            'image': ClearableFileInput(attrs={
                'accept': 'image/*'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'A bit about the product...',
                'rows': 5,
                'style': 'padding: 10px; max-height: 300px; width: 100%;'
            }),
            'price': forms.TextInput(attrs={
                'placeholder': 'Price...',
                'style': 'padding: 4px; width: 100%;'
            }),
            'shop_category': forms.Select(attrs={
                'style': 'padding: 4px; width: 100%;'
            }),
            'status': forms.Select(attrs={
                'style': 'padding: 4px; width: 100%;'
            }),
        }
        labels = {
            'title': 'Title:',
            'item': 'Item:',
            'description': 'Description:',
            'price': 'Price:',
            'shop_category': 'Shop Category:',
        }

    def __init__(self, *args, **kwargs):
        super(ShopForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.image:
            self.fields['image_display'] = forms.ImageField(required=False, initial=self.instance.image, widget=forms.FileInput)


class ImageForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=GalleryCategory.objects.all())

    class Meta:
        model = Images
        fields = ('image', 'title', 'description', 'category', 'status')
        widgets = {
            'image': ClearableFileInput(attrs={
                'accept': 'image/*'
            }),
            'title': forms.TextInput(attrs={
                'placeholder': 'Title...',
                'style': 'padding: 4px; width: 100%;'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'A bit about the product...',
                'rows': 5,
                'style': 'padding: 10px; max-height: 300px; width: 100%;'
            }),
            'category': forms.Select(attrs={
                'style': 'padding: 4px; width: 100%;'
            }),
            'status': forms.Select(attrs={
                'style': 'padding: 4px; width: 100%;'
            }),
        }
        labels = {
            'title': 'Title:',
            'description': 'Description:',
            'category': 'Category:',
        }

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        # Set the initial value of the image field
        if self.instance and self.instance.image:
            self.fields['image_display'] = forms.ImageField(required=False, initial=self.instance.image, widget=forms.FileInput)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('title', 'image', 'description', 'live_link', 'git_link', 'status')
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title...',
                'style': 'padding: 4px; width: 100%;'
            }),
            'image': ClearableFileInput(attrs={
                'accept': 'image/*'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'A bit about the product...',
                'rows': 5,
                'style': 'padding: 10px; max-height: 300px; width: 100%;'
            }),
            'live_link': forms.URLInput(attrs={
                'placeholder': 'Live Link...',
                'style': 'padding: 4px; width: 100%;'
            }),
            'git_link': forms.URLInput(attrs={
                'placeholder': 'Live Link...',
                'style': 'padding: 4px; width: 100%;'
            }),
            'status': forms.Select(attrs={
                'style': 'padding: 4px; width: 100%;'
            }),
        }
        labels = {
            'title': 'Title:',
            'description': 'Description:',
            'live_link': 'Live Link:',
            'git_link': 'Git Link:',
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        # Set the initial value of the image field
        if self.instance and self.instance.image:
            self.fields['image_display'] = forms.ImageField(required=False, initial=self.instance.image, widget=forms.FileInput)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'excerpt', 'image', 'status')
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title...',
                'style': 'padding: 4px; width: 100%;'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'A bit about the product...',
                'rows': 10,
                'style': 'padding: 10px; max-height: 500px; width: 100%;'
            }),
            'excerpt': forms.TextInput(attrs={
                'placeholder': 'Excerpt...',
                'style': 'padding: 4px; max-height: 250px; width: 100%;'
            }),
            'image': ClearableFileInput(attrs={
                'accept': 'image/*'
            }),
            'status': forms.Select(attrs={
                'style': 'padding: 4px; width: 100%;'
            }),
        }
        labels = {
            'title': 'Title:',
            'content': 'Content:',
            'excerpt': 'Excerpt:',
        }

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        # Set the initial value of the image field
        if self.instance and self.instance.image:
            self.fields['image_display'] = forms.ImageField(required=False, initial=self.instance.image, widget=forms.FileInput)
