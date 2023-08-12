from django.db import models
from datetime import datetime, date


class BlogPost(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    Subtitle = models.CharField(max_length=50)
    author = models.CharField(max_length=25, null=True, blank=True, default="Coder's Club")
    content_summary = models.TextField(max_length=1000)
    slug = models.CharField(max_length=150)
    first_heading = models.CharField(max_length=100)
    first_paragraph = models.TextField(max_length=1500)
    second_heading = models.CharField(max_length=100)
    second_paragraph = models.TextField(max_length=1500)
    blog_image = models.ImageField(
        null=True, blank=True, upload_to="static-images/Blog")
    slider_image1 = models.ImageField(
        null=True, blank=True, upload_to="static-images/Blog")
    slider_image2 = models.ImageField(
        null=True, blank=True, upload_to="static-images/Blog")
    slider_image3 = models.ImageField(
        null=True, blank=True, upload_to="static-images/Blog")
    slider_image4 = models.ImageField(
        null=True, blank=True, upload_to="static-images/Blog")
    slider_image5 = models.ImageField(
        null=True, blank=True, upload_to="static-images/Blog")
    timeStamp = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title + " by " + self.author
