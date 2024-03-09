from django.shortcuts import render,redirect
from . import forms
# Create your views here.

def add_post(request):
    if request.method=='POST': # user post request koreche
        post_form=forms.PostForm(request.POST) # user er post request data ekhane capture krlm.
        if post_form.is_valid(): #post kra dt valid kina check .!
            post_form.save() # jdi valid hy. database a save krbo
            return redirect('add_post') 
    else: # user normally website a gle blank form pbe !!! 
        post_form=forms.PostForm()
    return render(request, 'add_post.html',{'form':post_form})
