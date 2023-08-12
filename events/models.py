from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class EventManager(models.Manager):
    def registration_open(self):
        return self.filter(deadline__gt=timezone.now())

class Event(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    deadline = models.DateTimeField()
    criteria = models.CharField(max_length=150) # criteria of participation (who can participate)
    picture = models.ImageField(default='\static-images\events\event1.jpg', upload_to='events_pics', blank=True)

    objects = EventManager()

    def __str__(self):
        return self.name

    def is_registration_open(self):
        return self.deadline > timezone.now()
    
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(default='\\teams_logos\TeamBTC.png', upload_to='teams_logos', blank=True)

    def __str__(self):
        return self.name

class EventParticipation(models.Model):
    TEAM_SIZE_CHOICES = [
        (1, 'One Member'),
        (2, 'Two Members'),
        (3, 'Three Members'),
        (4, 'Four Members'),
    ]

    RANKING_CHOICES = [
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5, 'Fifth'),
    ]

    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    members = models.ManyToManyField(User)
    team_lead = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_lead')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='applications')
    team_size = models.IntegerField(choices=TEAM_SIZE_CHOICES)
    rank = models.PositiveSmallIntegerField(choices=RANKING_CHOICES, null=True, blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    cover_picture = models.ImageField(default='\participations_coverpics\TeamBTC.png', upload_to='participations_coverpics', blank=True)

    def __str__(self):
        return f"{self.event}: {self.team} ({self.team_size})"


