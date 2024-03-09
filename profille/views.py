from django.shortcuts import render,redirect
from . import forms
# Create your views here.

def add_profile(request):
    if request.method=='POST':
        profile_form=forms.ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('add_profile') #here add_author url name , love it
    else:
        profile_form=forms.ProfileForm()
    return render(request, 'add_profile.html',{'form':profile_form})
