from .models import Profile
from django import forms
from django.forms import DateInput
from django.contrib.auth.models import User


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
            'bio': forms.Textarea(attrs={
                'placeholder': 'Tell a bit about yourself...',
                'rows': 5,
            }),
        }
