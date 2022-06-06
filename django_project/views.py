# from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def greeting(request):
  context = {
    'greeting': 'Olá! Este é um exemplo do uso de templates. :)',
    'today': datetime.now()
  }
  return render(request, 'greeting.html', context)