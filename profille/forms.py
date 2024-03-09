from   django import forms
from . models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields='__all__'
        # sb field nea ekta form create kre dbe...
        # exclude= []
        # fields=['name','abc]

        