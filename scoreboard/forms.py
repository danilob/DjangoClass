from django import forms

from scoreboard.models import Team, SoccerPlayer

from django.core.exceptions import ValidationError


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'coach']
        #exclude = ['',...]

    def clean_coach(self):
        data = self.cleaned_data['coach']
        if not (data):
            raise ValidationError("É obrigatório adicionar o treinador.")

        return data

class SoccerPlayerForm(forms.ModelForm):
    class Meta:
        model = SoccerPlayer
        fields = '__all__'