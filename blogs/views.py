from django.shortcuts import render
from blogs.models import BlogPost


def home(request):
    allblog_post = BlogPost.objects.all()
    context = {'allblog_post': allblog_post}
    return render(request, "blogs/blogs.html", context)


def selected(request, id):
    post_selected = BlogPost.objects.filter(sno=id)[0]
    return render(request, "blogs/blogsSelected.html", {'post_selected': post_selected})
