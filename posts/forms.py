from   django import forms
from . models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields='__all__'
        # sb field nea ekta form create kre dbe...
        # exclude= []
        # fields=['name','abc]

        