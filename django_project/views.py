# from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from datetime import datetime
def greeting(request):
  week_days = ['Seg','Ter','Qua','Qui','Sex','Sáb','Dom']
  context = {
    'greeting': 'Olá! seja bem vindo!',
    'today': timezone.now(),
    'week_days': week_days 
  }
  return render(request, 'greeting.html', context)


def view_about(request):
  week_days = ['Seg','Ter','Qua','Qui','Sex','Sáb','Dom']
  context = {
    'greeting': 'Olá! seja bem vindo!',
    'today': timezone.now(),
    'week_days': week_days,
    'about': "Meu nome é Danilo desenvolvi está página utilizando Django."
  }
  return render(request, 'about.html', context)


def manual_form(request):
  if request.method == 'POST':
    name = request.POST['name']
    dt_nasc = request.POST['dt_nasc'] #formato aaaa-mm-dd
    dt_nasc_date = datetime.strptime(dt_nasc,'%Y-%m-%d')
    age = int((datetime.today() - dt_nasc_date).days/365)
    context = {
      'name': name,
      'age': age,
    }
    return render(request, 'result.html', context)
  context = {}
  return render(request, 'manual-form.html', context)

from .forms import NameDateForm
def django_form(request):
  if request.method == 'POST':
    form = NameDateForm(request.POST)
    if form.is_valid():
      dt_nasc_date = form.cleaned_data['dt_nasc'] #date
      age = int((datetime.today().date() - dt_nasc_date).days/365)
      context = {
        'name': form.cleaned_data['name'],
        'age': age,
      }
      return render(request, 'result.html', context)
  else:
        form = NameDateForm()
  context = {
    'form': form,
  }
  return render(request, 'django-form.html', context)