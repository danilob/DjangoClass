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

def remove_team(request,name):
    try:
        team = Team.objects.get(name=name)
        team.delete()
    except Exception as e:
        print(e)
    return redirect(reverse('scoreboard:list_team'))

from django.shortcuts import redirect
from django.urls import reverse

def change_team(request,name):
  team = Team.objects.get(name=name)
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