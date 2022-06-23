from django.shortcuts import render

from scoreboard.forms import TeamForm
def django_form_model(request):
  if request.method == 'POST':
    form = TeamForm(request.POST)
    if form.is_valid():
      model = form.save(commit=False)
      model.save()
      context = {
          'instance' : model,
          'model' : model.__class__.__name__
      }
      return render(request, 'scoreboard/success.html', context)
  else:
        form = TeamForm()
  context = {
    'form': form,
  }
  return render(request, 'scoreboard/django-form-model.html', context)


from scoreboard.models import Team
def list_team(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'scoreboard/list-team.html', context)

from django.shortcuts import redirect
from django.urls import reverse

from django.core.exceptions import ObjectDoesNotExist

def change_team(request,name):
  try:
    team = Team.objects.get(name=name)
  except ObjectDoesNotExist:
    return redirect(reverse('scoreboard:list_team'))
  if request.method == 'POST':
    form = TeamForm(request.POST,instance=team)
    if form.is_valid():
      model = form.save(commit=False)
      model.save()
      return redirect(reverse('scoreboard:list_team'))
  else:
        form = TeamForm(instance=team)
  context = {
    'form': form,
    'team': team,
  }
  return render(request, 'scoreboard/change-team.html', context)


def remove_team(request,name):
    try:
        team = Team.objects.get(name=name)
        team.delete()
    except ObjectDoesNotExist:
        pass
    return redirect(reverse('scoreboard:list_team'))


from scoreboard.forms import SoccerPlayerForm

def create_soccerplayer(request):
  if request.method == 'POST':
    form = SoccerPlayerForm(request.POST)
    if form.is_valid():
      model = form.save(commit=False)
      model.save()
      context = {
          'instance' : model,
          'model' : model.__class__.__name__
      }
      return render(request, 'scoreboard/success.html', context)
  else:
        form = SoccerPlayerForm()
  context = {
    'form': form,
  }
  return render(request, 'scoreboard/create-soccerplayer.html', context)


from scoreboard.models import SoccerPlayer
def list_soccerplayer(request):
    soccerplayers = SoccerPlayer.objects.all()
    context = {
        'soccerplayers': soccerplayers
    }
    return render(request, 'scoreboard/list-soccerplayer.html', context)


def change_soccerplayer(request,id):
  try:
    soccerplayer = SoccerPlayer.objects.get(id=id)
  except ObjectDoesNotExist:
    return redirect(reverse('scoreboard:list_soccerplayer'))
  if request.method == 'POST':
    form = SoccerPlayerForm(request.POST,instance=soccerplayer)
    if form.is_valid():
      model = form.save(commit=False)
      model.save()
      return redirect(reverse('scoreboard:list_soccerplayer'))
  else:
        form = SoccerPlayerForm(instance=soccerplayer)
  context = {
    'form': form,
    'soccerplayer': soccerplayer,
  }
  return render(request, 'scoreboard/change-soccerplayer.html', context)



def remove_soccerplayer(request,idsp):
    try:
        soccerplayer = SoccerPlayer.objects.get(id=idsp)
        soccerplayer.delete()
    except ObjectDoesNotExist:
        pass
    return redirect(reverse('scoreboard:list_soccerplayer'))