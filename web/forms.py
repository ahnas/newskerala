from django import forms
from django.forms.widgets import EmailInput, Textarea, TextInput
from versatileimagefield.fields import \
    SizedImageCenterpointClickDjangoAdminField

from .models import Comment, Contact, News, Newsletter


class NewsForm(forms.ModelForm):
    featured_image = SizedImageCenterpointClickDjangoAdminField()

    class Meta:
        model = News
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
            'email': EmailInput(attrs={'class': 'required form-control', 'placeholder': 'Email'}),
            'phone': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Phone'}),
            'subject': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Subject'}),
            'message': Textarea(attrs={'class': 'required form-control','rows':'4'}),
        }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Name'}),
            'place': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Place'}),
            'number': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Whatsapp Number'}),
            'district': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Type District'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['news','time','approved']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Name'}),
            'comment': Textarea(attrs={'class': 'required form-control','placeholder': 'Comment'}),
        }
