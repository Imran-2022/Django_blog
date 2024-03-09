from   django import forms
from . models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields='__all__'
        # sb field nea ekta form create kre dbe...
        # exclude= []
        # fields=['name','abc]

        