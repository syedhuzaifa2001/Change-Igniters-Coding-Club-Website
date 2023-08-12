from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'subject', 'message', 'submitted_at')

admin.site.register(Contact, ContactAdmin)