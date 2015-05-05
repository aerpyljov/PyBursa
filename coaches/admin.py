from django.contrib import admin

from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Pesonal Info', {'fields': ['user', 'gender', 'date_of_birth', 'image']}),
        ('Contact Info', {'fields': ['phone', 'address', 'skype']}),
        (None, {'fields': ['description']})
    ]
    list_display = ('user', 'admin_name', 'skype', 'admin_email', 'admin_thumbnail')
    list_filter = ['gender']
    search_fields = ['user']


admin.site.register(Coach, CoachAdmin)
