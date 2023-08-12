from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        local_time = timezone.localtime(self.submitted_at, timezone=timezone.get_fixed_timezone(300))
        if local_time.date() != timezone.localdate():
            # Display date only if it's not today
            formatted_time = local_time.strftime("%B %d, %Y")
        else:
            # Display time only if it's today
            formatted_time = local_time.strftime("%I:%M %p")
        return self.name + f" ({self.subject}) - {formatted_time}"