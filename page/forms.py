from django import forms
from .models import Posting, Comment

class PostingForm(forms.ModelForm):
    title = forms.CharField(label='제목')
    content = forms.CharField(label='내용', widget=forms.Textarea)

    class Meta:
        model = Posting
        fields = ['title', 'content',]

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='')
    
    class Meta:
        model = Comment
        fields = ['content',]