from django import forms


class PostForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput,
    )
    photo = forms.ImageField()
    content = forms.CharField(
        widget=forms.Textarea,
    )
