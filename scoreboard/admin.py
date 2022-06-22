from django.contrib import admin

from scoreboard.models import Team

class TeamAdmin(admin.ModelAdmin):
    pass

admin.site.register(Team, TeamAdmin)

from scoreboard.models import Color

class ColorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Color, ColorAdmin)

from scoreboard.models import SoccerPlayer

class SoccerPlayerAdmin(admin.ModelAdmin):
    pass

admin.site.register(SoccerPlayer, SoccerPlayerAdmin)


from scoreboard.models import Match

class MatchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Match, MatchAdmin)

from scoreboard.models import PlayGame

class PlayGameAdmin(admin.ModelAdmin):
    pass

admin.site.register(PlayGame, PlayGameAdmin)

