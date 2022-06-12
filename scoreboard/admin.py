from django.contrib import admin

from scoreboard.models import Team, Color, Match, SoccerPlayer, PlayGame

class TeamAdmin(admin.ModelAdmin):
    pass

admin.site.register(Team, TeamAdmin)

class ColorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Color, ColorAdmin)

class SoccerPlayerAdmin(admin.ModelAdmin):
    pass

admin.site.register(SoccerPlayer, SoccerPlayerAdmin)



class MatchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Match, MatchAdmin)


class PlayGameAdmin(admin.ModelAdmin):
    pass

admin.site.register(PlayGame, PlayGameAdmin)