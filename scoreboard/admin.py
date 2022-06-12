from django.contrib import admin

from scoreboard.models import Team

class TeamAdmin(admin.ModelAdmin):
    pass

admin.site.register(Team, TeamAdmin)
