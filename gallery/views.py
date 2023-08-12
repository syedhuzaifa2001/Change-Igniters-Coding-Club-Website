from django.shortcuts import render
from gallery.models import Gallery,GalleryItem


def home(request):
    allgallery_post = Gallery.objects.all()
    galleryitem_post = GalleryItem.objects.all()
    context = {'allgallery_post':allgallery_post,"galleryitem_post":galleryitem_post}
    return render(request, "gallery/gallery.html",context)

def galleryselected(request,Gallery_slug):
    gallery_selected = Gallery.objects.filter(Gallery_slug=Gallery_slug)[0]
    galleryitem_post = GalleryItem.objects.filter(gallery=gallery_selected.id)
    context = {"gallery_selected":gallery_selected,"galleryitem_post":galleryitem_post}
    return render(request, "gallery/galleryselected.html",context)