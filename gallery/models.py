from django.db import models
from events.models import Event

# Create your models here.

class Gallery(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='gallery')
    title = models.CharField(max_length=100)
    #title_id = models.AutoField(primary_key=True)
    second_title = models.TextField(max_length=150)
    slider_image1 = models.ImageField(null=True,blank=True,upload_to="static-images/gallery/gallery_pics")
    slider_image2 = models.ImageField(null=True,blank=True,upload_to="static-images/gallery/gallery_pics")
    slider_image3 = models.ImageField(null=True,blank=True,upload_to="static-images/gallery/gallery_pics")
    slider_image4 = models.ImageField(null=True,blank=True,upload_to="static-images/gallery/gallery_pics")
    cover_image = models.ImageField(upload_to='static-images/gallery/event_gallery_covers/')
    Gallery_slug = models.CharField(max_length=100)

    def __str__(self) :
        return f"{self.title} ({self.event})"


class GalleryItem(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='items')
    GalleryImage = models.ImageField(upload_to='static-images/gallery/event_gallery/')
    video = models.FileField(upload_to='static-images/gallery/event_gallery/', null=True, blank=True)

    def __str__(self):
        return f"Gallery Item ({self.gallery.title})"