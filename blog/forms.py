from .models import Review
from django import forms


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
