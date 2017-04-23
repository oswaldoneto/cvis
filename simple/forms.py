

from django import forms


class InputForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your own or paste some peace of text here...'}))