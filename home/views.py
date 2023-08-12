from django.shortcuts import render
from blogs.models import BlogPost
from gallery.models import Gallery


def home(request):
    context = {'blog_posts': BlogPost.objects.all(), 'allgallery_post': Gallery.objects.all()}
    return render(request, "home/home.html", context)

def about(request):
    return render(request, "home/about.html")
