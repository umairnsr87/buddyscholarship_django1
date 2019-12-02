from django.shortcuts import render
from .models import blog

# Create your views here.
def index(request):
    return render(request,'buddyscholarship_html/index.html',{})


def blogs(request):
    blog_data=blog.objects.all()
    context={
        "data":blog_data
             }
    return render(request,'buddyscholarship_html/blogs.html',context)
