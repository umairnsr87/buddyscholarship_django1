from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext

from .models import blog,college,cities
from django.views.generic import DetailView
from django.http import Http404

# Create your views here.
def index(request):
    blog_data = blog.objects.all().order_by( '-publish_date' )
    context = {
        "data": blog_data
    }
    return render(request,'buddyscholarship_html/index.html',context)


def blogs(request):
    blog_data=blog.objects.all().order_by('-publish_date')
    context={
        "data":blog_data
             }
    return render(request,'buddyscholarship_html/blogs.html',context)

def about(request):
    return render( request, 'buddyscholarship_html/about.html',{})


def admissions(request):
    return render( request, 'buddyscholarship_html/admissions.html',{})



class PostDetail(DetailView):
    model = blog
    template_name = 'buddyscholarship_html/post_detail.html'





