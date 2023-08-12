from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class UserProfile(models.Model):
    EMPLOYMENT_CHOICES = (
        ('Internee', 'Internee'),
        ('Full-time Job', 'Full-time Job'),
        ('Part-time Job', 'Part-time Job'),
        ('Freelancer', 'Freelancer'),
        ('None', 'None'),
    )

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    CITY_CHOICES = (
        ('Karachi', 'Karachi'),
        ('Hyderabad', 'Hyderabad'),
        ('Jamshoro', 'Jamshoro'),
    )

    CATEGORY_CHOICES = (
        ('Undergraduate', 'Undergraduate'),
        ('Postgraduate', 'Postgraduate'),
    )

    BATCH_CHOICES = (
        ('2022', '2022'),
        ('2021', '2021'),
        ('2020', '2020'),
        ('Older', 'Older'),
    )

    DEPARTMENT_CHOICES = (
        ('BCIT', 'BCIT'),
        ('SE', 'SE'),
        ('CIS', 'CIS'),
    )   

    UNIVERSITY_CHOICES = (
        ('NED University', 'NED University'),
        ('Mehran University', 'Mehran University'),
        ('Karachi University', 'Karachi University'),
    )     
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    city = models.CharField(max_length=20, choices=CITY_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    batch = models.CharField(max_length=20, choices=BATCH_CHOICES)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    university = models.CharField(max_length=100, choices=UNIVERSITY_CHOICES)
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES)
    contact_number = models.CharField(max_length=20)
    facebook_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    profile_picture = models.ImageField(default='https://t3.ftcdn.net/jpg/03/46/83/96/360_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg', upload_to='profile_pics', blank=True)

    def get_year(self):
        if self.batch == 'Older':
            return self.batch

        current_year = datetime.date.today().year
        year_diff = current_year - int(self.batch)

        if year_diff % 10 == 1 and year_diff != 11:
            return f"{year_diff}st"
        elif year_diff % 10 == 2 and year_diff != 12:
            return f"{year_diff}nd"
        elif year_diff % 10 == 3 and year_diff != 13:
            return f"{year_diff}rd"
        else:
            return f"{year_diff}th"

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Domain(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class ClubApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='applications')
    domains = models.ManyToManyField(Domain, blank=True)
    portfolio_link = models.URLField(blank=True, null=True)
    applied_date = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(blank=True, null=True)

    def __str__(self):
        local_time = timezone.localtime(self.applied_date, timezone=timezone.get_fixed_timezone(300))
        if local_time.date() != timezone.localdate():
            # Display date only if it's not today
            formatted_time = local_time.strftime("%B %d, %Y")
        else:
            # Display time only if it's today
            formatted_time = local_time.strftime("%I:%M %p")
        domains_list = [d.name for d in self.domains.all()]            
        return f"{self.user.profile.name} - {self.position} ({', '.join(domains_list)}) - {formatted_time}"
    
class ClubMembership(models.Model):
    POSITION_CHOICES = (
        ('Team Lead', 'Team Lead'),
        ('Team Member', 'Team Member'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memberships')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='memberships')
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='memberships')
    application = models.OneToOneField(ClubApplication, on_delete=models.CASCADE, related_name='memberships', null=True)

    def is_team_lead(self):
        return self.position == 'Team Lead'
    
    def __str__(self):
        return f"{self.user.username} - {self.position} - {self.domain}"

