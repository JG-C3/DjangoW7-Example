from django import forms
from django import forms
from .models import Posting

class PostingForm(forms.ModelForm):
    title = forms.CharField(label="제목")
    content = forms.CharField(label="내용", widget=forms.Textarea)

    class Meta:
        model = Posting
        fields = ['title', 'content',]