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