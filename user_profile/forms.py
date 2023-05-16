from .models import Profile, Order
from django import forms
from django.forms import DateInput
from django.contrib.auth.models import User
from django.forms.widgets import ClearableFileInput


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('fiName', 'laName', 'email', 'image', 'bio',)
        widgets = {
            'fiName': forms.TextInput(attrs={
                'placeholder': 'First name...',
                'style': 'padding: 4px; width: 100%;'
            }),
            'laName': forms.TextInput(attrs={
                'placeholder': 'Last name...',
                'style': 'padding: 4px; width: 100%;'
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Email Address...',
                'style': 'padding: 4px; width: 100%;'
            }),
            'image': ClearableFileInput(attrs={
                'accept': 'image/*'
            }),
            'bio': forms.Textarea(attrs={
                'placeholder': 'Tell a bit about yourself...',
                'rows': 5,
                'style': 'padding: 10px; max-height: 300px; width: 100%;'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.image:
            self.fields['image'].initial = self.instance.image.url

    def save(self, commit=True):
        profile = super().save(commit=False)
        if commit:
            if self.cleaned_data.get('image'):
                profile.image = self.cleaned_data['image']
            profile.user = self.instance.user
            profile.save()
        return profile


class CreateOrderForm(forms.ModelForm):
    order_number = forms.UUIDField(widget=forms.HiddenInput())

    class Meta:
        model = Order
        fields = ['profile']

    def save(self, commit=True):
        order = super().save(commit=False)
        order.user = self.instance.user
        order.order_number = self.cleaned_data['order_number']
        if commit:
            order.save()
        return order
