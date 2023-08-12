from django.contrib import admin
from .models import UserProfile, Domain, ClubApplication, ClubMembership, Position
from django.contrib.auth.models import User

class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(Domain)

admin.site.register(Position)

class ClubMembershipInline(admin.StackedInline):
    model = ClubMembership
    extra = 1   

    # def get_formset(self, request, obj=None, **kwargs):
    #     formset = super().get_formset(request, obj, **kwargs)
    #     formset.form.base_fields['user'].initial = obj.user
    #     formset.form.base_fields['position'].initial = obj.position
    #     formset.form.base_fields['domain'].initial = obj.domains.all().first()
    #     return formset

    def get_initial(self, request):
        initials = super().get_initial(request)
        # Get the current club application instance
        application_id = request.resolver_match.kwargs.get("object_id")
        if application_id:
            try:
                application = ClubApplication.objects.get(pk=application_id)
                initials['user'] = application.user
                initials['position'] = application.position
                initials['domain'] = application.domains.all().first()
            except ClubApplication.DoesNotExist:
                pass
        return initials    

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "domain":
            # Get the current club application instance
            application_id = request.resolver_match.kwargs.get("object_id")
            if application_id:
                try:
                    application = ClubApplication.objects.get(pk=application_id)
                    # Filter the domain choices based on the selected application's domains
                    kwargs["queryset"] = application.domains.all()
                except ClubApplication.DoesNotExist:
                    pass
        elif db_field.name == "user":
            # Get the current club application instance
            application_id = request.resolver_match.kwargs.get("object_id")
            if application_id:
                try:
                    application = ClubApplication.objects.get(pk=application_id)
                    # Filter the domain choices based on the selected application's domains
                    kwargs["queryset"] = User.objects.filter(id=application.user.id)
                except ClubApplication.DoesNotExist:
                    pass

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ClubApplicationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Applicant Information', {
            'fields': ('user', 'position', 'portfolio_link', 'applied_date', 'domains'),
        }),
        ('Application Status', {
            'fields': ('accepted',),
        }),        
    )
    readonly_fields = ('user', 'position', 'portfolio_link', 'applied_date', 'domains')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj.accepted:
            self.inlines = [ClubMembershipInline]
        else:
            self.inlines = []
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        # Call the parent implementation of save_model() first
        super().save_model(request, obj, form, change)

        # If the 'accepted' field is set to False, delete the associated ClubManagement object
        if not obj.accepted:
            try:
                club_membership = ClubMembership.objects.get(application=obj)
                club_membership.delete()
            except ClubMembership.DoesNotExist:
                pass

admin.site.register(ClubApplication, ClubApplicationAdmin)

class ClubMembershipAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'position', 'domain', 'application')

admin.site.register(ClubMembership, ClubMembershipAdmin)