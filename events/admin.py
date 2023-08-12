from django.contrib import admin
from .models import Event, Team, EventParticipation

admin.site.register(Team)

class EventParticipationAdmin(admin.ModelAdmin):
    readonly_fields = ('team', 'team_size', 'team_lead', 'members', 'event', 'applied_at')
    # list_display = ('cover_picture',)

admin.site.register(EventParticipation, EventParticipationAdmin)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_open',)

    def registration_open(self, obj):
        return obj.is_registration_open()

    registration_open.short_description = 'Registration Open?'

    @admin.display(boolean=True)
    def registration_open(self, obj):
        return obj.is_registration_open()
    