from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    coach = models.CharField(max_length=150,null=True,blank=True,help_text="é o professor do time")

    class Meta:
      ordering = ["coach"]
      verbose_name = "Time"
      verbose_name_plural = "Times"

    def __str__(self):
      return f'Time:{self.name.upper()}'

class Color(models.Model):
    teams      = models.ManyToManyField(Team)
    definition = models.CharField(max_length=40,unique=True)

    class Meta:
        ordering = ["definition"]
        verbose_name_plural = "Colors"

    def __str__(self):
        return self.definition.lower()

class SoccerPlayer(models.Model):
    team     = models.ForeignKey(Team,on_delete=models.SET_NULL,null=True)
    name     = models.CharField(max_length=150)
    number   = models.IntegerField()

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "SoccerPlayers"
        constraints = [
            models.UniqueConstraint(
                fields=('team', 'name','number'), name='unique_team_name_number'
            )
        ]

    def __str__(self):
        return self.name.upper()


class Match(models.Model):
    team_home      = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='related_home_team')
    team_visiting  = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='related_visiting_team')
    tournament     = models.CharField(max_length=100)
    goal_home      = models.IntegerField(default=0)
    goal_visiting  = models.IntegerField(default=0)
    date           = models.DateTimeField()

    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Matchs"
        constraints = [
            models.UniqueConstraint(
                fields=('tournament', 'team_home','team_visiting'), name='unique_tournament_team_home_visiting'
            )
        ]

    def __str__(self):
        return f'{self.tournament.upper()}: {self.team_home.name.upper()} x {self.team_visiting.name.upper()}'


class PlayGame(models.Model):
    GOL = 'GL'
    LAT_DIR = 'LD'
    LAT_ESQ = 'LE'
    ZAG = 'ZA'
    VOL = 'VL'
    MEIA = 'ME'
    ATAC = 'TK'
    POSITIONS = (
        (GOL,'Goleiro'),
        (LAT_DIR,'Lateral Direita'),
        (LAT_ESQ,'Lateral Esquerda'),
        (ZAG,'Zagueiro'),
        (VOL,'Volante'),
        (MEIA,'Meia'),
        (ATAC,'Atacante'),
    )

    soccerplayer = models.ForeignKey(SoccerPlayer,on_delete=models.CASCADE)
    match        = models.ForeignKey(Match,on_delete=models.CASCADE)
    position     = models.CharField(max_length=2,choices=POSITIONS)
    
    class Meta:
        verbose_name_plural = "Play Games"
        constraints = [
            models.UniqueConstraint(
                fields=('soccerplayer', 'match','position'), name='unique_soccerplayer_match_position'
            )
        ]

    def __str__(self):
        return f'{self.soccerplayer.name.upper()} - {self.get_position_display().upper()}'
