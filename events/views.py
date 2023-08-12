from django.shortcuts import render, redirect
from django.utils import timezone
from .models import EventParticipation, Team, Event
from django.contrib.auth.models import User

def home(request):
    return render(request, "events/events.html", {'events': Event.objects.all(), 'events_copy': Event.objects.all()})


def leaderboard(request):
    return render(request, "events/leaderboard.html")


def apply(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        event_id = request.POST.get('event_id')        
        participation = request.POST.get('participation')
        
        if Team.objects.filter(name=team_name).exists():
            team = Team.objects.get(name=team_name)
        else:
            team = Team.objects.create(name=team_name)

        if participation == 'Individual':
            event_participation = EventParticipation.objects.create(
                team = team,
                team_lead = request.user,
                team_size = 1,
                event = Event.objects.get(id=event_id),        
            )
            
            event_participation.members.add(request.user)
            event_participation.applied_at = timezone.now()
            event_participation.save()
            success_message = "Application submitted!"
            return render(request, 'events/apply.html', {'success_message': success_message})
               
        elif participation == 'Team':
            members = request.POST.getlist('members')
            event_participation = EventParticipation.objects.create(
                team = team,
                event = Event.objects.get(id=event_id),
                team_size = 0,
                team_lead = User.objects.get(username=members[0])
            )            
            team_size = 0            
            print(members)
            for member_username in members:
                if User.objects.filter(username=member_username).exists():
                    member = User.objects.get(username=member_username)
                    event_participation.members.add(member)
                    team_size += 1
                    if team_size == 1:
                        event_participation.team_lead = member
            event_participation.team_size = team_size
            event_participation.applied_at = timezone.now()
            event_participation.save()
            success_message = "Application submitted!"
            return render(request, 'events/apply.html', {'success_message': success_message, 'events': events})            
    else:
        if not request.user.is_authenticated:
            return redirect('account-login')
        else:
            events = Event.objects.registration_open()
            return render(request, "events/apply.html", {'events': events})