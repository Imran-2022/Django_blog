from django.shortcuts import render
from posts.models import Post

def home(request):
    data = Post.objects.all()
    # print(data)
    # for i in data:
        # print(i.title,i.category)
        # for j in i.category.all():
        #     print(j)
    
    return render(request,'home.html', {'data':data})

