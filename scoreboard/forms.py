from django import forms

from scoreboard.models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        #exclude = ['',...]