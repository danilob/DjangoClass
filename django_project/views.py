from django.http import HttpResponse

def greeting(request):
   return HttpResponse("Olá, meu nome é Danilo")