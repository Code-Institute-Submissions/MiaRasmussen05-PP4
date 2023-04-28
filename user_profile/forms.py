from .models import Profile
from django import forms
from django.forms import DateInput
from django.contrib.auth.models import User
from django.forms.widgets import ClearableFileInput


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('fiName', 'laName', 'email', 'birth_date', 'image', 'bio',)
        widgets = {
            'fiName': forms.TextInput(attrs={
                'placeholder': 'First name...',
            }),
            'laName': forms.TextInput(attrs={
                'placeholder': 'Last name...',
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Email Address...',
            }),
            'birth_date': DateInput(attrs={
                'type': 'date'
            }),
            'image': ClearableFileInput(attrs={
                'accept': 'image/*'
            }),
            'bio': forms.Textarea(attrs={
                'placeholder': 'Tell a bit about yourself...',
                'rows': 5,
            }),
        }

    def save(self, commit=True):
        profile = super().save(commit=False)
        if commit:
            profile.user = self.instance
            profile.save()
        return profile

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # Set the initial value of the image field
        if self.instance and self.instance.image:
            self.fields['image_display'] = forms.ImageField(required=False, initial=self.instance.image, widget=forms.FileInput)
